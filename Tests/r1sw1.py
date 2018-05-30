from netmiko import ConnectHandler
from datetime import datetime

R1 = {
	
	'device_type':'cisco_ios',
	'ip':'10.1.1.1',
	'username':'admin',
	'password':'zaq12wsx',
	'verbose':False,
}
SW1 = {
	
	'device_type':'cisco_ios',
	'ip':'10.1.1.7',
	'username':'admin',
	'password':'zaq12wsx',
	'verbose':False,
}

devices = [R1,SW1]
start_time=datetime.now()
for a_device in devices:
	net_connect=ConnectHandler(**a_device)
	output=net_connect.send_command("show arp")

	print (a_device['device_type'])
	print ("\n\n>>>>>>>>>>>Device:"+a_device['device_type']+"<<<<<<<<<<<<<")
	print(output)
	print (">>>>>>>>>>>>END<<<<<<<<<<<<<<<<")

end_time=datetime.now()
total_time=end_time - start_time

print("Elapsed time: ",total_time)