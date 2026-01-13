import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, ReadOnly

def matmul3x3(A,B):
    C = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            s = 0
            for k in range(3):
                s += A[i][k] * B[k][j]
            C[i][j] = s
    return C

def drive_input(dut,a,b):
    #a = array of 3 ints
    #b = array of 3 ints
    for i in range(3):
        dut.a_in[i].value = int(a[i])
        dut.b_in[i].value = int(b[i])

def readout(dut):
    C = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            C[i][j] = dut.acc_out[i][j].value.to_signed()
    return C

async def reset_array(dut):
    cocotb.start_soon(Clock(dut.clk,10, unit="ns").start())
    dut.rst.value = 1
    dut.clr.value = 0
    drive_input(dut,[0,0,0],[0,0,0])

    for _ in range(3):
        await RisingEdge(dut.clk)

    dut.rst.value = 0
    await RisingEdge(dut.clk)

async def matmul1(dut): #test matmul for a*b
    A = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    B = [
        [9,8,7],
        [6,5,4],
        [3,2,1]
    ]

    expected = matmul3x3(A,B)

    reset_array(dut)

    for t in range(7): #takes 7 cycles to cycle all inputs through array
        a = []
        b = []
        
        for r in range(3):
            k = t - r
            a.append(A[r][k] if 0 <= k < 3 else 0)

        for c in range(3):
            k = t - c
            b.append(A[k][c] if 0 <= k < 3 else 0)

        drive_input(dut,a,b)
        await RisingEdge

    got = readout(dut)
    dut._log.info(f"Result C = {got}")

    assert got == expected, f"Mismatch!\nExpected: {expected}\nGot: {got}"


    














