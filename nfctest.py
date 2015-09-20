import nfc
import nfc.ndef
import nfc.clf

import logging
from observable import Observable

class ReadWriteTag(Observable):
    "Exposes methods to read and write the NDEF sector of a NFC tag. Duh!"

    def __init__(self):
        self.reader_path = "tty:AMA0:pn532"
        self.ndef_data = None

    def __on_rdwr_startup(self, targets):
        return targets

    def __on_rdwr_connect(self, tag):
        if tag.ndef:
            record = tag.ndef.message[0]
            if record.type == "urn:nfc:wkt:T":
                ndef_text = nfc.ndef.TextRecord(record).text
                self.ndef_data = ndef_text
                self.trigger("ndef_data_read", ndef_text)
            else:
                logging.warning('NDEF data not of type "urn:nfc:wkt:T" (text)')
        else:
            logging.info('No NDEF data found')
        return True # Wait until the tag has been removed

    def run_once(self):
        clf = nfc.ContactlessFrontend(self.reader_path)
        try:
            return clf.connect(rdwr={
                'on-startup': self.__on_rdwr_startup,
                'on-connect': self.__on_rdwr_connect,
            })
        finally:
            clf.close()

    def run_infinite(self):
        while self.run_once():
            logging.info('--- Ready to read another tag ---')

if __name__ == '__main__':
    reader = ReadWriteTag().run_infinite()