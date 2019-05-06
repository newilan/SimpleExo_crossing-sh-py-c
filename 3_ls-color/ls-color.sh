#!/bin/bash

set -eu

# Colors:
RED='\e[0;31m'
GREEN='\e[0;32m'
YELLOW='\e[0;33m'
D_BLUE='\e[0;34m'
PURPLE='\e[0;35m'
L_BLUE='\e[0;36m'

IFS="
"

toggle=0

for i in $(ls -A);
do

    choice=$(( toggle % 6 ))
    case $choice in
        0) echo -e "${RED}$i" ;;
        1) echo -e "${GREEN}$i" ;;
        2) echo -e "${YELLOW}$i" ;;
        3) echo -e "${D_BLUE}$i" ;;
        4) echo -e "${PURPLE}$i" ;;
        5) echo -e "${L_BLUE}$i" ;;
        *) echo "ERROR" ;;
    esac

    toggle=$(( $toggle + 1 ))
done

