`default_nettype none
`timescale 1ns/1ns

module sysarray #(
    parameter int A_W = 8,
    parameter int B_W = 8,
    parameter int ACC_W = 18
) (
    input logic clk,
    input logic rst,
    input logic clr,
    input logic signed [A_W-1:0] left [0:2],
    input logic signed [B_W-1:0] top [0:2],
    output logic signed [ACC_W-1:0] out [0:2][0:2]
)
    
    logic signed [A_W-1:0] a_bus [0:2][0:3]; //r,c ordering, need one extra col for pass out
    logic signed [B_W-1:0] b_bus [0:3][0:2];

    assign a_bus[0][0] = left[0]; //wire first buses to receive data
    assign a_bus[1][0] = left[1];
    assign a_bus[2][0] = left[2];
    assign b_bus[0][0] = top[0];
    assign b_bus[0][1] = top[1];
    assign b_bus[0][2] = top[2];

    //ROW 0
    pe #(.A_W(A_W),.B_W(B_W),.ACC_W(ACC_W)) pe1 (
        .clk(clk), 
        .rst(rst), 
        .clr(clr),
        .a_in(a_bus[0][0]), 
        .b_in(b_bus[0][0]),
        .a_out(a_bus[0][1]),
        .b_out(b_bus[1][0]),
        .acc_out(out[0][0])
    )

    pe #(.A_W(A_W),.B_W(B_W),.ACC_W(ACC_W)) pe2 (
        .clk(clk), 
        .rst(rst), 
        .clr(clr),
        .a_in(a_bus[0][1]), 
        .b_in(b_bus[0][1]),
        .a_out(a_bus[0][2]),
        .b_out(b_bus[1][1]),
        .acc_out(out[0][1])
    )

    pe #(.A_W(A_W),.B_W(B_W),.ACC_W(ACC_W)) pe3 (
        .clk(clk), 
        .rst(rst), 
        .clr(clr),
        .a_in(a_bus[0][2]), 
        .b_in(b_bus[0][2]),
        .a_out(a_bus[0][3]),
        .b_out(b_bus[1][2]),
        .acc_out(out[0][2])
    )

    //ROW 1
    pe #(.A_W(A_W),.B_W(B_W),.ACC_W(ACC_W)) pe4 (
        .clk(clk), 
        .rst(rst), 
        .clr(clr),
        .a_in(a_bus[1][0]), 
        .b_in(b_bus[1][0]),
        .a_out(a_bus[1][1]),
        .b_out(b_bus[2][0]),
        .acc_out(out[1][0])
    )

    pe #(.A_W(A_W),.B_W(B_W),.ACC_W(ACC_W)) pe5 (
        .clk(clk), 
        .rst(rst), 
        .clr(clr),
        .a_in(a_bus[1][1]), 
        .b_in(b_bus[1][1]),
        .a_out(a_bus[1][2]),
        .b_out(b_bus[2][1]),
        .acc_out(out[1][1])
    )

    pe #(.A_W(A_W),.B_W(B_W),.ACC_W(ACC_W)) pe6 (
        .clk(clk), 
        .rst(rst), 
        .clr(clr),
        .a_in(a_bus[1][2]), 
        .b_in(b_bus[1][2]),
        .a_out(a_bus[1][3]),
        .b_out(b_bus[2][2]),
        .acc_out(out[1][2])
    )

    //ROW 2
    pe #(.A_W(A_W),.B_W(B_W),.ACC_W(ACC_W)) pe7 (
        .clk(clk), 
        .rst(rst), 
        .clr(clr),
        .a_in(a_bus[2][0]), 
        .b_in(b_bus[2][0]),
        .a_out(a_bus[2][1]),
        .b_out(b_bus[3][0]),
        .acc_out(out[2][0])
    )

    pe #(.A_W(A_W),.B_W(B_W),.ACC_W(ACC_W)) pe8 (
        .clk(clk), 
        .rst(rst), 
        .clr(clr),
        .a_in(a_bus[2][1]), 
        .b_in(b_bus[2][1]),
        .a_out(a_bus[2][2]),
        .b_out(b_bus[3][1]),
        .acc_out(out[2][1])
    )

    pe #(.A_W(A_W),.B_W(B_W),.ACC_W(ACC_W)) pe9 (
        .clk(clk), 
        .rst(rst), 
        .clr(clr),
        .a_in(a_bus[2][2]), 
        .b_in(b_bus[2][2]),
        .a_out(a_bus[2][3]),
        .b_out(b_bus[3][2]),
        .acc_out(out[2][2])
    )
endmodule