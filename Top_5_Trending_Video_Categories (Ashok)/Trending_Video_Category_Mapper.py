import csv

i = open("..\data\USvideos.csv","r")
reader = csv.reader(i)
o = open("storedata_category.txt","w")
start = True

for line in reader:
    if start:
        start = False
    else:
        print line[2] + "\t" + line[3]
        o.write(line[2] + "\t" + line[3] + "\n")

i.close()
o.close()    