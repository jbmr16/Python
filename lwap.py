from netmiko import ConnectHandler

def config_ports(modulex,lwap):
	port=""
	for z in range(1,(modulex+1)):           #For production range(1,4)
		for x in range (0,4):      #For production range(1,38)
			port = port + ("interface Ethernet "+str(z)+"/"+str(x)+ #For production /0/
				"\n"+"switchport access vlan "+lwap+"\n"+
				"switchport mode access\n"+
				"switchport port-security\n"+
				"switchport port-security max 3\n"+
				"switchport voice vlan 11\n"+
				"logging event link-status\n"+
				"spanning-tree portfast\n"+
				"description [LWAP]\n"
				)
	net_connect=ConnectHandler(**a_device)
	net_connect.send_config_set(port)
	print("Port configuration completed")


file = open ("/home/server/Desktop/python/lwap","r")
devices = (file.read())
mylist = devices.split('\n')
mylist2 = []
for e in range(len(mylist)):
	mylist2.append(mylist[e].split(','))
devices =[]
port = ""


for y in range(0 ,len(mylist)):
	SW={
		'device_type':'cisco_ios',
		'ip':mylist2[y][0],
		'username':'admin',
		'password':'zaq12wsx',
		'verbose':False,
	}
	devices.append(SW)

interface1 = 'Et1/3'
interface2 = 'Et2/3'
interface3 = 'Et3/3'
c=0
for a_device in devices:
	print ("\nDevice:"+a_device['ip'])
	net_connect=ConnectHandler(**a_device)
	print(net_connect.find_prompt())
	output=net_connect.send_command("show interface status")

	if(output.find(interface3) != -1):
		module = 3
		config_ports(module,mylist2[c][1])
		c = c + 1
	elif(output.find(interface2) != -1):
		module = 2
		config_ports(module,mylist2[c][1])
		c = c + 1
	elif(output.find(interface1) != -1):
		module = 1
		config_ports(module,mylist2[c][1])
		c = c + 1
	else:
		print("Switch Model incorrect")







