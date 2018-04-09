i = open("mapperoutput.txt","r")
o = open("sortedoutput.txt","w")

lines = i.readlines()
lines.sort(reverse=True)

for line in lines:
	o.write(line)
	# print(line)

i.close()
o.close()