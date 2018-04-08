i = open("storedata_category.txt","r")
o = open("sorteddata_category.txt","w")

lines = i.readlines()
lines.sort()

for  line in lines:
    o.write(line)

i.close()
o.close()    