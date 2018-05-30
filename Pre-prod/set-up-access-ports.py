from netmiko import ConnectHandler

def config_ports(modulex):
	port=""
	for z in range(1,(modulex+1)):           #For production range(1,4)
		for x in range (0,4):      #For production range(1,38)
			port = port + ("interface Ethernet "+str(z)+"/"+str(x)+ #For production /0/
				"\n"+"switchport access vlan 10\n"+
				"switchport mode access\n"+
				"switchport port-security\n"+
				"switchport port-security max 3\n"+
				"switchport voice vlan 11\n"+
				"logging event link-status\n"+
				"spanning-tree portfast\n"+
				"description [ACCESS-PORTS-NEW-5]\n"
				)
	print(port)		
	net_connect=ConnectHandler(**a_device)
	net_connect.send_config_set(port)
	print("Port configuration completed")


file = open ("/home/server/Desktop/python/devices","r")
devices = (file.read())
mylist = devices.split(',')
devices =[]
port = ""

for y in range(0 ,len(mylist)):
	SW={
		'device_type':'cisco_ios',
		'ip':mylist[y],
		'username':'admin',
		'password':'zaq12wsx',
		'verbose':False,
	}
	devices.append(SW)

interface1 = 'Et1/3'
interface2 = 'Et2/3'
interface3 = 'Et3/3'
for a_device in devices:
	print ("\nDevice:"+a_device['ip'])
	net_connect=ConnectHandler(**a_device)
	print(net_connect.find_prompt())
	output=net_connect.send_command("show interface status")

	if(output.find(interface3) != -1):
		module = 3
		config_ports(module)
	elif(output.find(interface2) != -1):
		module = 2
		config_ports(module)
	elif(output.find(interface1) != -1):
		module = 1
		config_ports(module)
	else:
		print("Switch Model incorrect")







