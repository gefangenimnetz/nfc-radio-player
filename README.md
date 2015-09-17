# nfc-radio-player
A raspberry pi based LoFi audio player using Volumio (raspberry image) and a PN532 breakout board

# NFC Tags
Are JSON formatted and contain one root element with a `source` of type `usb | spotify | playlist` and the source `url`.
```
{
    "source": "usb",
    "Muckemacher/Diggidiggi Bambam"
}
```

# Todo
- [x] Control MPD via buttons
- [ ] Implement NFC Tag reading via polling (JSON)
- [ ] Purge play queue and play selected album/title/playlist
- [ ] Connect amplifier via I²C and set volume
    - Problem: There are two volumes; Volumio (mpd audio out) and the amplifier’s. Which one to set?
- [ ] Find power supply: one powerplug for two voltages: 5V for Raspberry, 12V for amplififer board
- [ ] Play spotify sources (via SPOP)
- [ ] Built casing
- [ ] UI to write to tags (select source, input url, click write button and add tag to reader/writer)
