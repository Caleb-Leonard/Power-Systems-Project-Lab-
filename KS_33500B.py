#Author: Caleb Leonard
#Use: PyVisa to control Keysight 33500B Waveform Generator
#Look at Keysight 33220A Programmer's Manual for SCPI ref

import pyvisa as pyv

rm = pyv.ResourceManager()
instr = rm.list_resources()

def WaveGenConnect(address):
	adg = rm.open_rsources(address)
	print(adg.query("*IDN?")
	return adg

def UnitVp-p_Setup
	ch_list = [1, 2]
	command = ""
	if channel not in ch_list:
		raise Exception("Sorry, Channel Not Available")
	else:
		command = ":SOURce" + str(channel) + ":VOLTage:UNIT VPP"
		inst.write(command)
def PWM_Setup(inst, channel, freq, ampl, offset, duty)
	ch_list = [1, 2]
	command = ""
	if channel not in ch_list:
		raise Exception("Sorry, Channel Not Available")
	else:
		command = ":SOURce" + str(channel) + ":APPLy:SQUare " + str(freq) + "," + str(ampl) + " VPP" + "," + str(offset)
		inst.write(command)
		command = ":SOURce" + str(channel) + ":FUNCtion:SQUare:DCYCle " + str(freq)
		inst.write(command)

def OUT_ON(inst, channel):
	ch_list = [1, 2]
	command = ""
	if channel not in ch_list:
		raise Exception("Sorry, Channel Not Available")
	else:
		command = "OUTPut" + str(channel) + " 1"
		inst.write(command)

def OUT_OFF(inst, channel):
	ch_list = [1, 2]
	command = ""
	if channel not in ch_list:
		raise Exception("Sorry, Channel Not Available")
	else:
		command = "OUTPut" + str(channel) + " 0"
		inst.write(command)