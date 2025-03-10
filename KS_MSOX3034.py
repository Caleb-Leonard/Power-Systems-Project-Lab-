#Author: Caleb Leonard
#Use: PyVisa to control Keysight MSOX3034 Oscilloscope

import pyvisa as pyv

rm = pyv.ResourceManager()
instr = rm.list_resources()

def OSCOPE_Connect(address):
	ks = rm.open_resources(address)
	print(ks.query("*IDN?")
	return ks

def OSCOPE_Stop(inst):
	inst.write(":STOP")

def OSCOPE_Single(inst):
	inst.write(":SINGle")

def OSCOPE_RUN(inst):
	inst.write(":RUN")

def OSCOPE_TimeBase(inst, Time_div):
	command = ":TIMEbase:SCALe " + str(div)
	inst.write(command)

def OSCOPE_SaveWF(inst, source):
	command = "WAVeform:SOURce " + source
	inst.write(command)
	command = "WAVeform:BYTeorder MSBFirst" 
	inst.write(command)
	command = "WAVeform:FORMat ASCii" 
	inst.write(command)
	command = "WAVeform:POINts MAXimum " 
	inst.write(command)

	command = "WAVeform:PREAmble?"
	inst.write(command)
	command = "WAVeform:DATA?"
	inst.write(command)
	
	return preamble, data



	
