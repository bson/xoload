# xoload
Trivial XO load capacitor calculator.

For example, a [Microchip MCP7940N](https://www.microchip.com/en-us/product/mcp7940n) has an oscillator pin capacitance of 3pF.
We use an [ECS-.327-9-16-TR](https://ecsxtal.com/products/crystals/surface-mount-crystals/ecs-327-9-16-tr/) crystal that wants a load capacitance of 9pF.
Because of the very close proximity of our placement and practically nonexistent traces we don't include the trace capacitance.
```
$ xoload 9 3
15.0
$
```
We need two 15pF load capacitors.
