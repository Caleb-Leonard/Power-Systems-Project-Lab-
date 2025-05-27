#Author: Caleb Leonard
#Use: PyVisa to control Keysight N3300A
#Electronic Load Programmer's Manual: https://www.keysight.com/us/en/assets/9018-01307/programming-guides/9018-01307.pdf?success=true
#PyVISA Library Docs: https://pyvisa.readthedocs.io/en/stable/index.html

import pyvisa as pyv

rm = pyv.ResourceManager()
instr = rm.list_resources()

def ELoadConnect(address):
	adg = rm.open_resource(address)
	print(adg.query("*IDN?"))
	return adg

#WIP
def Source_Current(inst)
	command = 
	inst.write(command)

#WIP
def Source_Resistance(inst)
	command = 
	inst.write(command)

#WIP
def Source_Voltage(inst)
	command = 
	inst.write(command)

#WIP
def Measure_Power(inst)
	command = 
	power = 
	return power

#WIP
def Measure_Current(inst)
	command = 
	current = 
	return current

#WIP
def Measure_Voltage(inst)
	command = 
	voltage = 
	return voltage

