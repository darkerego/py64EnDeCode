#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author Darkerego, references:
# http://stackoverflow.com/questions/2941995/python-ignore-incorrect-padding-error-when-base64-decoding
"""
╔╗ ┌─┐┌─┐┌─┐ ╔═╗╔╗╔  ╔╦╗╔═╗╔═╗┌─┐╔╦╗╔═╗
╠╩╗├─┤└─┐├┤ 6║╣ ║║║ / ║║║╣ ║  │ │ ║║║╣ 
╚═╝┴ ┴└─┘└─┘4╚═╝╝╚╝/ ═╩╝╚═╝╚═╝└─┘═╩╝╚═╝
"""

import base64,sys,binascii,sys

def b64encode(s, altchars=None):
    """Encode a string using Base64.

    s is the string to encode.  Optional altchars must be a string of at least
    length 2 (additional characters are ignored) which specifies an
    alternative alphabet for the '+' and '/' characters.  This allows an
    application to e.g. generate url or filesystem safe Base64 strings.

    The encoded string is returned.
    """
    # Strip off the trailing newline
    encoded = binascii.b2a_base64(s)[:-1]
    if altchars is not None:
        return _translate(encoded, {'+': altchars[0], '/': altchars[1]})
    return encoded

def urlsafe_b64decode(s):
    """Encode a string using a url-safe Base64 alphabet.
       If TypeError 'Incorrect Padding" is raised, fix it.
    """
    s = str(s).strip()
    try:
        return base64.b64decode(s)
    except TypeError:
        padding = len(s) % 4
        if padding == 1:
 
            return ''
        elif padding == 2:
            s += b'=='
        elif padding == 3:
            s += b'='
        return base64.b64decode(s)

def main():
    doWhat = sys.argv[1]
    s = str(raw_input("Paste stuff to en/de/code :"))
    if doWhat == "-e":
        encoded = b64encode(s, altchars=None)
        print("\n"+"Base64 Encoded Text: "+"\n"+"%s" % encoded)
    elif doWhat == "-d":
         decoded = urlsafe_b64decode(s)           
         print("\n"+"Base64 Decoded Text:"+"\n"+"%s" % decoded)

if __name__ == "__main__":
    main()
