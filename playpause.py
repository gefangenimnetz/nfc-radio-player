#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import subprocess
import time
import json
import logging
import os

import nfctest
from bottle import Bottle, run, get, post, request, template

# set numbering to chipset type
GPIO.setmode(GPIO.BCM)

# Buttons (GPIO inputs) "real" pull-down resistors should be in place
INPUT_button_playPause = 9
INPUT_button_stop = 25
INPUT_button_next = 11
INPUT_button_prev = 8

GPIO.setup(INPUT_button_playPause, GPIO.IN)
GPIO.setup(INPUT_button_stop, GPIO.IN)
GPIO.setup(INPUT_button_next, GPIO.IN)
GPIO.setup(INPUT_button_prev, GPIO.IN)

# LED output pins
OUTPUT_led_playing = 4
GPIO.setup(OUTPUT_led_playing, GPIO.OUT)

mpd_music_library_path = '/var/lib/mpd/music/'

def led_blink(amount):
    # for amount ...
    GPIO.output(OUTPUT_led_playing, 0)
    time.sleep(0.1)
    GPIO.output(OUTPUT_led_playing, 1)
    time.sleep(0.1)
    GPIO.output(OUTPUT_led_playing, 0)
    time.sleep(0.1)
    GPIO.output(OUTPUT_led_playing, is_mpd_currently_playing())

def is_mpd_currently_playing():
    mpc_output = subprocess.check_output(['mpc', 'status'])
    playingString = '[playing]'
    return playingString in mpc_output

def get_mpd_vol_as_int():
    mpc_output = subprocess.check_output(['mpc', 'volume'])
    vol = mpc_output.replace('volume: ', '')
    vol = vol.replace('%', '')
    return vol

def toggle_play_pause(channel):
    print('play/pause')
    mpc_output = subprocess.check_output(['mpc', 'toggle'])
    GPIO.output(OUTPUT_led_playing, is_mpd_currently_playing())   

def stop(channel):
    print('stop')
    mpc_output = subprocess.check_output(['mpc', 'stop'])
    GPIO.output(OUTPUT_led_playing, 0)

def next(channel):
    print('next song')
    mpc_output = subprocess.check_output(['mpc', 'next'])
    led_blink(2)

def prev(channel):
    print('previous song')
    mpc_output = subprocess.check_output(['mpc', 'prev'])
    led_blink(2)

def playViaMPD(command):
    subprocess.call(['mpc', 'clear'])
    subprocess.check_output('mpc ls "' + command + '" | mpc add', shell=True)
    subprocess.call(['mpc', 'play'])

def playViaSPOP(command):
    print(command)

def parse_ndef(ndef):
    tagPlayInfo = json.loads(ndef)
    command = None
    service = None

    if tagPlayInfo['source'] == 'usb':
        service = 'mpd'
        command = 'USB/' + tagPlayInfo['url']
    if tagPlayInfo['source'] == 'playlist':
        service = 'mpd'
        command = 'USB/' + tagPlayInfo['url']
    if tagPlayInfo['source'] == 'spotify':
        service = 'spop'
        command = tagPlayInfo['url']

    fullCommandPath = mpd_music_library_path + command
    if os.path.isdir(fullCommandPath) or os.path.isfile(fullCommandPath):
        if service == 'mpd':
            playViaMPD(command)
        if service == 'spop':
            playViaSPOP(command)
    else:
        mpc_output = subprocess.check_output(['mpc', 'pause'])
        time.sleep(0.5)
        subprocess.call('mpg123 -q ' + os.path.dirname(os.path.abspath(__file__)) + '/sounds/not_found.mp3', shell=True)
        time.sleep(0.5)
        mpc_output = subprocess.check_output(['mpc', 'play'])

# Detect button events
GPIO.add_event_detect(INPUT_button_playPause, GPIO.RISING, callback=toggle_play_pause, bouncetime=500)
GPIO.add_event_detect(INPUT_button_stop, GPIO.RISING, callback=stop, bouncetime=500)
GPIO.add_event_detect(INPUT_button_next, GPIO.RISING, callback=next, bouncetime=200)
GPIO.add_event_detect(INPUT_button_prev, GPIO.RISING, callback=prev, bouncetime=200)

# Initially set playing LED
GPIO.output(OUTPUT_led_playing, is_mpd_currently_playing())

# Write a Tag (via web app interface)
app = Bottle()

def path_to_dict(path):
    name = os.path.basename(path)
    d = {'text': name}
    if os.path.isdir(path):
        d['type'] = "folder"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
    else:
        if os.path.isfile(path) and name.lower().endswith(('.mp3')) and not name.lower().startswith(('.')):
            d['type'] = "file"
        else:
            d['li_attr'] = { "style": "display: none;" }
            
    return d

@app.get('/')
def show_interface():
    sources = ['usb', 'spotify']
    tree = json.dumps(path_to_dict(mpd_music_library_path + '/USB'), sort_keys=True)
    return template('writetag-server/index.tpl', sources=sources, tree=tree)

@app.post('/')
def write_tag():
    source = request.forms.get('source')
    url = request.forms.get('url')
    if source and url:
        return "<p>You selected %s and %s</p>" % (source, url)
    else:
        return "<p>Login failed.</p>"

# app.run(host = '192.168.188.36', port = '8080')

# Read a Tag
reader = nfctest.ReadWriteTag()
reader.on("ndef_data_read", parse_ndef)

while reader.run_once():
    logging.info('Waiting for NFC tags')

# Exiting
logging.info('Exit')
GPIO.output(OUTPUT_led_playing, GPIO.LOW)
GPIO.cleanup()
subprocess.call(['mpc', 'stop'])
