#!/bin/bash

set -e

day=$1
if [ -z $day ]; then
    echo "Usage: ${BASH_SOURCE[0]} <day>"
    exit 1
fi

session=$(cat .session)
if [ -z $session ]; then
    echo ".session file is empty"
    exit 1
fi

curl -fsSL -b "session=$session" "https://adventofcode.com/2023/day/$day/input" -o "inputs/day$day.txt"
