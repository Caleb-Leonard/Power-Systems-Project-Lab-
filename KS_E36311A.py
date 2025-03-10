#Author: Caleb Leonard
#Use: PyVisa to control Keysight E36311A Triple Output Power Supply

import pyvisa as pyv

rm = pyv.ResourceManager()
instr = rm.list_resources()

def PSConnect(address):
	ks = rm.open.resources(address)
	print(ks.query("*IDN?"))
	return ks

def Sel_Chan(inst, channel = -1):
	ch_list = [1, 2, 3]
	command = ""
	if channel not in ch_list:
		raise Exception("Sorry Channel Not Available")
	else: 
		command = ":INSTruments:SELect CH" + str(channel)
		inst.write(command)

def Volt_Set(inst, channel = -1, voltage = 0)
	ch_list = [1, 2, 3]
	command = ""
	if channel not in ch_list:
		raise Exception("Sorry Channel Not Available")
	else: 
		command = ":SOURce:VOLage:LEVel:IMMediate:AMPLitde" + str(voltage) + ",(@" + str(channel) +")"
		inst.write(command)

def Curr_Set(inst, channel = -1, current = 0)
	ch_list = [1, 2, 3]
	command = ""
	if channel not in ch_list:
		raise Exception("Sorry Channel Not Available")
	else: 
		command = ":SOURce:CURRent:LEVel:IMMediate:AMPLitde" + str(current) + ",(@" + str(channel) +")"
		inst.write(command)

def Out_ON(inst, channel = -1):
	ch_list = [1, 2, 3]
	command = ""
	result = 0
	if channel not in ch_list:
		raise Exception("Sorry Channel Not Available")
	else: 
		command = ":OUTPut:STATe 1,(@" + str(channel) + ")"
		inst.write(command)

def Out_OFF(inst, channel = -1):
	ch_list = [1, 2, 3]
	command = ""
	if channel not in ch_list:
		raise Exception("Sorry Channel Not Available")
	else: 
		command = ":OUTPut:STATe 0,(@" + str(channel) + ")"
		inst.write(command)

def Save_Disp(inst)
	command = ":HCOPy:SDUMp:DATA:FORMat PNG" 
	inst.write(command)
	command = ":HCOPy:SDUMp:DATA?" 
	inst.write(command)
