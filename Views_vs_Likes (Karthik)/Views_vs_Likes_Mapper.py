import csv
i = open("../data/USvideos.csv","r")
reader = csv.reader(i)
o = open("mapperoutput.txt","w")
start = True
ratio = 0
for l in reader:
    if not start:
        v_id = l[0]
        title = l[1]
        title = title.replace(","," ")
        v = float(l[5])
        l = float(l[6])
        if v > 0 and l > 0:
            ratio = (l/v)*100
            o.write (str(ratio)+","+ v_id+"++"+title+"++"+str(v)+"++"+str(l)+"\n")
    else:
        start = False
i.close()
o.close()