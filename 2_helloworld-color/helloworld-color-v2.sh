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

for i in $(printf 'Hello World !' | sed "s/\(.\)/\1\n/g");
#for i in $(printf 'Je mange une pomme rouge' | sed "s/\(.\)/\1\n/g");
do
    if [ "$i" == ' ' ]; then
        printf ' '
        continue
    fi

    choice=$(( toggle % 6 ))
    case $choice in
        0) printf "${RED}$i" ;;
        1) printf "${GREEN}$i" ;;
        2) printf "${YELLOW}$i" ;;
        3) printf "${D_BLUE}$i" ;;
        4) printf "${PURPLE}$i" ;;
        5) printf "${L_BLUE}$i" ;;
        *) echo "ERROR" ;;
    esac

    toggle=$(( $toggle + 1 ))
done

printf "\n"

