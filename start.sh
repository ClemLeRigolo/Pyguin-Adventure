#!/bin/bash
cd src
python3 "$(dirname "$(readlink -f "$0")")/main.py"
