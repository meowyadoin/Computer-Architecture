#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

cpu.load("/users/lambda_school_loaner_222/Desktop//Computer-Architecture/ls8/examples/mult.ls8")
cpu.run()