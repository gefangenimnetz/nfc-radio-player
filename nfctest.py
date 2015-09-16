import nfc
import nfc.ndef
import nfc.clf

import time

def on_connect(tag):
    if tag.ndef:
        record = tag.ndef.message[0]
        if record.type == "urn:nfc:wkt:T":
            textContent = nfc.ndef.TextRecord(record).text
            print(textContent)
        else:
            print("Not a text record")
    else:
        print('no ndef found')

rdwr_options = {
    'on-connect': on_connect
}

with nfc.ContactlessFrontend('tty:AMA0:pn532') as clf:
    tag = clf.connect(rdwr=rdwr_options)
