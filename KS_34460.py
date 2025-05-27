#Author: Caleb Leonard
#Use: PyVisa to control Keysight 34460 Digital Multimeter
#Multimeter Programmer's Manual: https://www.keysight.com/us/en/assets/9018-04842/service-manuals/9018-04842.pdf
#PyVISA Library Docs: https://pyvisa.readthedocs.io/en/stable/index.html

import pyvisa as pyv

rm = pyv.ResourceManager()
instr = rm.list_resources()

def DMMConnect(address):
	adg = rm.open_resource(address)
	print(adg.query("*IDN?"))
	return adg

def Save_Display(inst):
	command = "HCOPy:SDUMp:FORMat PNG"
	inst.write(command)
	command = "HCOPy:SDUMp:FORMat? "
	inst.query(command)

def Measure_Current(inst):
	command = "MEASure[:PRIMary]:CURRent:[:DC]?"
	inst.query(command)