i = open("final.txt","r")
o = open("trendingSorted.txt","w")

lines = i.readlines()
lines.sort(reverse=True)

for  line in lines:
    o.write(line)

i.close()
o.close()    