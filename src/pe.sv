`default_nettype none
`timescale 1ns/1ns

module pe #(
    parameter int A_W = 8, //gonna use int8 representation
    parameter int B_W = 8,
    parameter int ACC_W = 18
) (
    input logic clk, 
    input logic rst, //completely resets PE
    input logic clr, //reset accumulator
    input logic signed [A_W-1:0] a_in,
    input logic signed [B_W-1:0] b_in,
    output logic signed [A_W-1:0] a_out,
    output logic signed [B_W-1:0] b_out,
    output logic signed [ACC_W-1:0] acc_out
);

    localparam int PROD_W = A_W + B_W;
    logic signed [PROD_W-1:0] prod;

    assign prod = a_in * b_in;

    always_ff @(posedge clk) begin
        if (rst) begin
            acc_out <= '0;
            a_out <= '0;
            b_out <= '0;
        end else if (clr) begin
            acc_out <= '0;
            a_out <= a_in;
            b_out <= b_in;
        end else begin
            a_out <= a_in;
            b_out <= b_in;
            acc_out <= acc_out + $signed(prod);
        end
    end
endmodule