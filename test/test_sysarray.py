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
        dut.


@cocotb.test
async def matmul1(dut):
    print('yo')



