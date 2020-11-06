#!/bin/bash
rm -f *.out
for case in `ls *.in`; do
    python3 ../main.py < $case > "$case.out"
done;
