#!/usr/bin/env bash
cd me/kmom03/lab3/ || exit
e() { exit; }; export -f e
f() { exit 1; }; export -f f

echo "Run lab"
python3 answer.py

read -p "Press to view answer.py" answer
cat answer.py