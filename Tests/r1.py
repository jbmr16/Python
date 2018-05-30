from netmiko import ConnectHandler

R1 = {
	
	'device_type':'cisco_ios',
	'ip':'10.1.1.1',
	'username':'admin',
	'password':'zaq12wsx',
}
net_connect = ConnectHandler(**R1)
net_connect.find_prompt()
output = net_connect.send_command("show run | inc loggin")
output = net_connect.send_config_set(config_commands)

