n = open("o.txt","r")  # open file, read-only
s = open("s.txt", "w") # open file, write
lines = n.readlines()
#Sorts the data in alphabetical order
lines.sort()

for line in lines:
	s.write(line)
n.close()
s.close()
