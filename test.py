import logging
import nfctest

def doit(ndef):
    print(ndef)

reader = nfctest.ReadWriteTag()
reader.on("ndef_data_read", doit)
reader.run_infinite()