from netmiko import ConnectHandler

SW1 = {
	
	'device_type':'cisco_ios',
	'ip':'10.1.1.7',
	'username':'admin',
	'password':'zaq12wsx',
	'verbose':False,
}


SW2 = {
	
	'device_type':'cisco_ios',
	'ip':'10.1.1.8',
	'username':'admin',
	'password':'zaq12wsx',
	'verbose':False,
}

port = ""
devices = [SW1,SW2]
for y in range(1,4):

	for x in range (0,4):
		port = port + ("interface Ethernet "+str(y)+"/"+str(x)+
			"\n"+"switchport access vlan 10\n"+
			"switchport mode access\n"+
			"switchport port-security\n"+
			"switchport port-security max 3\n"+
			"switchport voice vlan 11\n"+
			"logging event link-status\n"+
			"spanning-tree portfast\n"+
			"description [ACCESS-PORTS]\n"
			)

print (port)

print("Do you want to continue?! y/n")
answer = input()

if(answer == 'y'):
	for a_device in devices:
		net_connect=ConnectHandler(**a_device)
		net_connect.send_config_set(port)
		vlan = net_connect.send_command("show vlan br")
		print (vlan)
else:
	print("Action terminated")

