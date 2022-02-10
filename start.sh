#!/bin/sh
cd src
python3 "$(dirname "$(readlink -f "$0")")/src/main.py"

