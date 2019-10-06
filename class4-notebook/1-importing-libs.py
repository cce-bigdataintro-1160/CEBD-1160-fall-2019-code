#!/usr/bin/env python3

import sys
import os

script_name = sys.argv[0]
is_file = os.path.isfile(script_name)
print(f'{script_name} is file? {is_file}')

import time
import random

for i in range(0, 10):
    time.sleep(1)
    print(random.randint(0, 50))
