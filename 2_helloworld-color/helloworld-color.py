#!/usr/bin/env python3

# Colors:
__RED__ = "\033[0;31m"
__GREEN__ = "\033[0;32m"
__YELLOW__ = "\033[0;33m"
__D_BLUE__ = "\033[0;34m"
__PURPLE__ = "\033[0;35m"
__L_BLUE__ = "\033[0;36m"

toggle = 0

my_string = "Hello World !"

for c in my_string :

    if c == ' ' :
        print(" ", sep='', end='')
        continue

    if toggle % 6 == 0:
        print(__RED__, c, sep='', end='')
    elif toggle % 6 == 1:
        print(__GREEN__, c, sep='', end='')
    elif toggle % 6 == 2:
        print(__YELLOW__, c, sep='', end='')
    elif toggle % 6 == 3:
        print(__D_BLUE__, c, sep='', end='')
    elif toggle % 6 == 4:
        print(__PURPLE__, c, sep='', end='')
    elif toggle % 6 == 5:
        print(__L_BLUE__, c, sep='', end='')
    else:
        print("ERROR")

    toggle = toggle + 1


print("")

