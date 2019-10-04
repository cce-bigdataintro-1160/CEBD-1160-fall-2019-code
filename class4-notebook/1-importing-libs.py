#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("myargument")
args = parser.parse_args()
print(args.myargument)

import sys
myargument = sys.argv[1]

import os
script_name = sys.argv[0]
os.path.isfile(script_name)

import time
time.sleep(10)

import random
print(random.randint(0, 50))
