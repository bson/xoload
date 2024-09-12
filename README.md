# Trivial XO load capacitor calculator

## Usage

```
$ xoload
Calculate load capacitor value.  Requires symmetric pin and trace capacitances.

Usage:

  xoload CL Cpin Ct

    CL = crystal specified load capacitance (required)
    Cpin = oscillator pin capacitance (required)
    Ct = parasitic trace capacitance (defaults to 0)
```

The loads are assumed symmetric, meaning both XO pins and traces have the same parasitic capacitance.

# Example

A [Microchip MCP7940N](https://www.microchip.com/en-us/product/mcp7940n) has an oscillator pin capacitance of 3pF.
If we use an [ECS-.327-9-16-TR](https://ecsxtal.com/products/crystals/surface-mount-crystals/ecs-327-9-16-tr/) crystal, it will require a load capacitance of 9pF.
Because of the very close proximity of our placement and practically nonexistent traces we don't include the trace capacitance.
```
$ xoload 9 3
15.0
$
```
We need two 15pF load capacitors.

# Installation

Clone this repo.
On Linux/MacOS,
```
install -m 755 ./xoload.py /usr/local/bin/xoload
```
