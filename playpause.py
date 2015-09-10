import RPi.GPIO as GPIO
import subprocess
import time

# set numbering to chipset type
GPIO.setmode(GPIO.BCM)

# Buttons (GPIO inputs)
# "real" pull-down resistors in place
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

# Detect button events
GPIO.add_event_detect(INPUT_button_playPause, GPIO.RISING, callback=toggle_play_pause, bouncetime=500)
GPIO.add_event_detect(INPUT_button_stop, GPIO.RISING, callback=stop, bouncetime=500)
GPIO.add_event_detect(INPUT_button_next, GPIO.RISING, callback=next, bouncetime=200)
GPIO.add_event_detect(INPUT_button_prev, GPIO.RISING, callback=prev, bouncetime=200)

try:

    #Initially set playing LED
    GPIO.output(OUTPUT_led_playing, is_mpd_currently_playing())

    while True:
        #We will do the NFC polling here
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    print 'keyboardinterrupt caught'
    GPIO.output(OUTPUT_led_playing, GPIO.LOW)
    GPIO.cleanup()
    subprocess.call(['mpc', 'stop'])
