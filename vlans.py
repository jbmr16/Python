from netmiko import ConnectHandler

with open("hello.csv") as f:
	output = f.read()
	vlans = output.split('\n')
	vlans.pop()

	for x in vlans:
		device = x.split(',')
		hostname = device[0]

		SW={
		'device_type':'cisco_ios',
		'ip':hostname,
		'username':'admin',
		'password':'zaq12wsx',
		'verbose':False,
		}
		print("Start configuring "+hostname)
		net_connect=ConnectHandler(**SW)
		portChannel = device[1]
		vlanx = device[2:]
		print(vlanx)
		y=0
		trunk=[]
		while y != len(vlanx):
			print("vlan "+ vlanx[y]+"\n"+"name "+ vlanx[y+1])
			net_connect.send_config_set("vlan "+ vlanx[y]+"\n"+"name "+ vlanx[y+1])
			trunk.append(vlanx[y])
			y +=2
		print("interface port-channel "+portChannel+"\n"+"switchport\n"+"switchport trunk allowed vlan add "+','.join(trunk))	
		net_connect.send_config_set("interface port-channel "+portChannel+"switchport\n"+"switchport trunk allowed vlan add "+','.join(trunk))
		print("Completed "+hostname)
