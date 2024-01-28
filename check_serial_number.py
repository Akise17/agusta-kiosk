import os, platform
def getMachine_addr():
	os_type = platform.system()
	if "Windows" in os_type:
		command = "wmic bios get serialnumber"
		serialnumber = os.popen(command).read().replace("\n","").replace("	","").replace(" ","")
	elif "Linux" in os_type:
		command = "cat /sys/firmware/devicetree/base/serial-number"
		serialnumber = os.popen(command).read().replace("\n","").replace("	","").replace(" ","")
	elif "Darwin" in os_type:
		command = "ioreg -l | grep IOPlatformSerialNumber"
		command = os.popen(command).read().replace("\n","").replace("	","").replace(" ","")
		command = ''.join(command)
		command = command.split('=')
		serialnumber = command[-1]

	return serialnumber
