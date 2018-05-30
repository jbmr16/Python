with open("hello.csv") as f:
	output = f.read()
	vlans = output.split(',')
	y=0
	while y != len(vlans):
		print("vlan "+ vlans[y] +"\n")
		print("description "+ vlans[y+1] +"\n")
		y +=2

