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

devices = [SW1,SW2]

file = open ("/home/server/Desktop/python/config.txt","r")
commands = (file.read())
print(commands)


print("Do you want to continue?! y/n")
answer = input()


if(answer == 'y'):
	for a_device in devices:
		print ("\nDevice:"+a_device['ip'])
		net_connect=ConnectHandler(**a_device)
		net_connect.send_config_set(commands)
		print ("\nCompleted")
else:
	print("Action terminated")