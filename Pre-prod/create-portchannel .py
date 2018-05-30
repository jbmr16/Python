from netmiko import ConnectHandler

with open("interfaces.csv") as f:
	output = f.read()
	interface = output.split('\n')
	interface.pop()

	for x in interface:
		device = x.split(',')
		hostname = device[0]

		SW={
		'device_type':'cisco_ios',
		'ip':hostname,
		'username':'admin',
		'password':'zaq12wsx',
		'verbose':False,
		}
		print("Creating portchannel in "+hostname)
		net_connect=ConnectHandler(**SW)
		portChannel = device[1]
		interf = device[2:]
	
		for y in interf:
			print("interface "+y+"\n"+"switchport \n"+"channel-group "+ portChannel +" mode active\n")
			net_connect.send_config_set("interface "+y+"\n"+"switchport \n"+"channel-group "+ portChannel +" mode active\n")
		print("interface port-channel "+portChannel+"\n"+"description [UPLINK] R1(Fast1/1)\n"+"switchport \n"+"switchport trunk encapsulation dot1q\n"+"switchport mode trunk\n"+"logging event link-status\n")
		net_connect.send_config_set("interface "+portChannel+"\n"+"description [UPLINK] R1(Fast1/1)"+"switchport \n"+"switchport trunk encapsulation dot1q\n"+"switchport mode trunk\n"+"logging event link-status\n")
	print("Completed")