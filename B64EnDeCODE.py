#!/usr/bin/env python
# Uncomplicated Base64 En/De/Coder
import base64
"""
╔╗ ┌─┐┌─┐┌─┐ ╔═╗╔╗╔  ╔╦╗╔═╗╔═╗┌─┐╔╦╗╔═╗
╠╩╗├─┤└─┐├┤ 6║╣ ║║║ / ║║║╣ ║  │ │ ║║║╣ 
╚═╝┴ ┴└─┘└─┘4╚═╝╝╚╝/ ═╩╝╚═╝╚═╝└─┘═╩╝╚═╝
"""
def enCODE():
    string=(input("Paste ASCII to Encode :"))
                               # Python 3+ will crash without 
    string=(str.encode(string))#this line
    enc = base64.b64encode(string).decode('utf-8')
    print ('\nResult:\n\n',enc,'\n')

def deCODE():
    dstring=(input("Paste Base64 to Decode: "))
    # Use this rather than "base64.b64decode(s)"
    de = base64.urlsafe_b64decode(dstring)
    print ('\nResult:\n\n',de,'\n')



while True:
    try:
        doWhat = int(input("Enter 0 to encode or 1 to decode: "))
    except ValueError:
        print("Dude...")
        
        continue
    else:
        if doWhat <= 1:
            break

if doWhat == 0:
    enCODE()
elif doWhat == 1:
    deCODE()
else:
    print("WTF?")
    exit(1)
