# nfc-radio-player
A raspberry pi based LoFi audio player using Volumio (raspberry image) and a PN532 breakout board

# NFC Tags
NDEF is used to store and read relevent infos from the tags. At this time no authorization or encryption is used at all.
Are JSON formatted and contain one root element with a `source` of type `usb | spotify | playlist` and the source `url`.
```
{
    "source": "usb",
    "Muckemacher/Diggidiggi Bambam"
}
```

# Todo
- [x] Control MPD via buttons
- [x] Implement NFC Tag reading via polling (JSON)
- [x] Purge play queue and play selected album/title/playlist
- [x] Change amplifier volume direcly in analog mode via poti.
    - Problem: Volumio WebUI will allow to change volume of Raspberry Pi (ignore for now!)
- [x] Find power supply: one powerplug for two voltages: 5V for Raspberry, 5V for amplififer board
- [ ] Find a way to switch power supply from mains to 6xAA. Best if this can happen automatically.
- [ ] Play directory vs single file. Automatic detection: `os.path.isfile("file.mp3") / os.path.isdir(folder)`
- [ ] Play spotify sources (via SPOP)
- [ ] Built case
- [ ] Solder to case using protoboard
- [ ] UI to write to tags (select source, input url, click write button and add tag to reader/writer) probably even with easy upload directly to the player (USB)
