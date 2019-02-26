#!/usr/bin/python

import spammer_class
spammer = spammer_class.Spammer()
spammer.tema = "Grab Spam"
try:
    spammer.main()
except KeyboardInterrupt:
    print spammer_class.color.FAIL+spammer_class.color.REVERSE+"\r[!][except] KeyboardInterrupt detected! Exiting . . ."+spammer_class.color.ENDC
    exit()

