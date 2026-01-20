# Mini-MMU: 3x3 Systolic Array in SystemVerilog for Quantized GEMM

A simple hardware accelerator that uses a 2D systolic array for matrix multiplication, inspired by the TPU's matrix multiply unit (MMU).

## Why this project?

I was reading through *In-Datacenter Performance Analysis of a Tensor Processing Unit* and became curious about how neural network workloads are accelerated in hardware. Systolic arrays are central to this process, so I decided to go about implementing a smaller version to learn how they work at RTL. I also wanted to investigate how different dataflows (output-stationary, weight-stationary) affect dataflow and performance.

## What this project does

- Implements a 3x3 output-stationary systolic array
- Supports int8 inputs with 18-bit accumulators
- Verified using cocotb in Python

## Architecture

- 9 processing elements (PEs) arranged in a 3x3 grid
- Each PE:
  - Has clock and reset signals
  - Takes incoming int8 values A and B as inputs
  - Multiplies A and B and adds product to accumulator register
  - Passes A value to the right and B down each cycle
  - Output remains stationary in accumulator register
  - Supports int8 inputs and 18-bit accumulators

## Timing

- Given the matrix multiply of $AB$, where A and B are 3x3 matrices, we stagger the rows of A and columns of B so that matrix elements are multiplied at the correct time in the systolic array
- For t = 0, t++:
  - For each row $r$ (zero indexed) of matrix A:
    - Define $k=t-r$
    - If $k\in [0,2]$, inject $A[r][k]$ into the array, otherwise inject 0
  - For each column $c$ (zero indexed) of matrix B:
    - Define $k=t-c$
    - If $k \in [0,2]$, inject $B[k][c]$ into the array, otherwise inject 0

The above is pretty hard to visualize, so I've drawn out the layout of the data:

```markdown
![timing](timing.jpg)
```
