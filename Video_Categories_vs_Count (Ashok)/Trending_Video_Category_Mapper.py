import csv

i = open("..\data\USvideos.csv","r")
reader = csv.reader(i)
o = open("storedata_category.txt","w")
start = True

for line in reader:
    if start:
        start = False
    else:
        print "Category id: " + line[3]
        o.write(line[3] + "\n")

i.close()
o.close()    