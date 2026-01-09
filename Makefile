TOPLEVEL_LANG = verilog
SIM = icarus
WAVES = 1

TOPLEVEL = pe

# Your Python test module.
# If your test file is test/test_pe.py, then MODULE=test.test_pe
MODULE = test.test_pe
VERILOG_SOURCES = $(PWD)/src/pe.sv
COMPILE_ARGS += -g2012

include $(shell cocotb-config --makefiles)/Makefile.sim
