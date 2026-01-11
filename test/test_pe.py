import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, ReadOnly, NextTimeStep, FallingEdge

@cocotb.test() 
async def reset(dut): #Test reset signal
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    dut.rst.value = 1 #set reset signal
    dut.clr.value = 0
    dut.a_in.value = 1
    dut.b_in.value = 1

    await RisingEdge(dut.clk)
    await ReadOnly()

    assert dut.acc_out.value.to_signed() == 0 #check if reset signal sets all PE outputs to 0
    assert dut.a_out.value.to_signed() == 0
    assert dut.b_out.value.to_signed() == 0

    await FallingEdge(dut.clk)
    dut.rst.value = 0 #update new reset signal on falling edge

    await RisingEdge(dut.clk)
    await ReadOnly()

    assert dut.acc_out.value.to_signed() == 1 #confirm rst = 0 gives us normal signals
    assert dut.a_out.value.to_signed() == 1
    assert dut.b_out.value.to_signed() == 1

@cocotb.test()
async def pe_1(dut): #Test result for pos * pos 
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    dut.rst.value = 1
    dut.clr.value = 0
    dut.a_in.value = 3
    dut.b_in.value = 2
    await RisingEdge(dut.clk)
    await ReadOnly()

    assert dut.acc_out.value.to_signed() == 0 #check that values have been reset
    assert dut.a_out.value.to_signed() == 0
    assert dut.b_out.value.to_signed() == 0

    await FallingEdge(dut.clk) #write on falling edge
    dut.rst.value = 0

    await RisingEdge(dut.clk)
    await ReadOnly()

    assert dut.acc_out.value.to_signed() == 6 #check that computation works
    assert dut.a_out.value.to_signed() == 3
    assert dut.b_out.value.to_signed() == 2


@cocotb.test()
async def pe_2(dut): #Test results for neg * pos
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    dut.rst.value = 1
    dut.clr.value = 0
    dut.a_in.value = -2
    dut.b_in.value = 2
    await RisingEdge(dut.clk)
    await ReadOnly()

    assert dut.acc_out.value.to_signed() == 0
    assert dut.a_out.value.to_signed() == 0
    assert dut.b_out.value.to_signed() == 0

    await FallingEdge(dut.clk)
    dut.rst.value = 0
    
    await RisingEdge(dut.clk)
    await ReadOnly()

    assert dut.acc_out.value.to_signed() == -4
    assert dut.a_out.value.to_signed() == -2
    assert dut.b_out.value.to_signed() == 2

@cocotb.test()
async def pe_3(dut): #test results for neg * neg
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    dut.rst.value = 1
    dut.clr.value = 0
    dut.a_in.value = -8
    dut.b_in.value = -8
    await RisingEdge(dut.clk)
    await ReadOnly()

    assert dut.acc_out.value.to_signed() == 0
    assert dut.a_out.value.to_signed() == 0
    assert dut.b_out.value.to_signed() == 0

    await FallingEdge(dut.clk)
    dut.rst.value = 0
    
    await RisingEdge(dut.clk)
    await ReadOnly()

    assert dut.acc_out.value.to_signed() == 64
    assert dut.a_out.value.to_signed() == -8
    assert dut.b_out.value.to_signed() == -8

@cocotb.test()
async def clear(dut): #test that clear sets accumulator to 0, but not outputs for a and b
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    dut.rst.value = 1
    dut.clr.value = 0
    dut.a_in.value = 0
    dut.b_in.value = 0

    await RisingEdge(dut.clk)
    await FallingEdge(dut.clk) 

    dut.rst.value = 0  #do some random computation
    dut.clr.value = 0
    dut.a_in.value = 7
    dut.b_in.value = -7
    
    await RisingEdge(dut.clk)
    await ReadOnly()

    assert dut.acc_out.value.to_signed() == -49 #do some random computation 
    assert dut.a_out.value.to_signed() == 7
    assert dut.b_out.value.to_signed() == -7

    await FallingEdge(dut.clk) 
    dut.clr.value = 1

    await RisingEdge(dut.clk)
    await ReadOnly()

    assert dut.acc_out.value.to_signed() == 0 #check that clear signal resets accumulated value but passes on a and b
    assert dut.a_out.value.to_signed() == 7
    assert dut.b_out.value.to_signed() == -7