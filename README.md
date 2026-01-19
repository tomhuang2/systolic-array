# Mini-MMU: 3x3 Systolic Array in SystemVerilog for Quantized GEMM
A simple hardware accelerator that uses a 2D systolic array for matrix multiplication, inspired by the TPU's matrix multiply unit (MMU).

## Why this project?
I was reading through *In-Datacenter Performance Analysis of a Tensor Processing Unit* and became curious about how neural network workloads are accelerated in hardware. Systolic arrays are central to this process, so I decided to go about implementing a smaller version to learn how they work at RTL. I also wanted to investigate how different dataflows (output-stationary, weight-stationary) affect dataflow and performance.

## What this project does
- Implements a 3x3 systolic array
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
- Operands are injected so that
