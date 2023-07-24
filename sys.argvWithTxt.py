#!/usr/bin/env python3
import sys
my_text_file = sys.argv[1]

with open(my_text_file, 'r') as f:
    f_cont = f.read()
print(f_cont)
