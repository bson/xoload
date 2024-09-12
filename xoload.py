#! /usr/bin/env python3

# Usage:
#   xoload CL Cpin Ct
#
# CL = Crystal specific load capacitance
# Cpin = oscillator pin capacitance
# Ct = parasitic trace capacitance (default 0)
#
# Calculates the value of two equal load capacitors for the oscillator.
#

import sys

if len(sys.argv) < 3:
    sys.stderr.write(
"""
Calculate load capacitor value.  Requires symmetric pin and trace capacitances.

Usage:

  xoload CL Cpin Ct

    CL = crystal specified load capacitance (required)
    Cpin = oscillator pin capacitance (required)
    Ct = parasitic trace capacitance (defaults to 0)

""")
    exit(0)


cl = (float)(sys.argv[1])
cpin = (float)(sys.argv[2])
ct = (float)(sys.argv[3]) if len(sys.argv) == 4 else 0.0

cx = 2 * cl - cpin - 2 * ct

print("%0.1f" % cx)
