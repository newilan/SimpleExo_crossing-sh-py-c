#!/usr/bin/env python3

import os

# Colors:
__RED__ = "\033[0;31m"
__GREEN__ = "\033[0;32m"
__YELLOW__ = "\033[0;33m"
__D_BLUE__ = "\033[0;34m"
__PURPLE__ = "\033[0;35m"
__L_BLUE__ = "\033[0;36m"

toggle = 0

#for l in os.listdir('.') :
for l in sorted(os.listdir('.')) :

    if toggle % 6 == 0:
        print(__RED__, l, sep='')
    elif toggle % 6 == 1:
        print(__GREEN__, l, sep='')
    elif toggle % 6 == 2:
        print(__YELLOW__, l, sep='')
    elif toggle % 6 == 3:
        print(__D_BLUE__, l, sep='')
    elif toggle % 6 == 4:
        print(__PURPLE__, l, sep='')
    elif toggle % 6 == 5:
        print(__L_BLUE__, l, sep='')
    else:
        print("ERROR")

    toggle = toggle + 1

