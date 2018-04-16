i = open("CategoryCount_TopicWise.txt","r")
o = open("Top5Trending.txt","w")

trending_dict = {}

lines = i.readlines()
lines.sort(reverse=True)

for  line in lines:
    data = line.strip().split("\t")
    if data != " " or data != None:
        cCount,cid = data    
        trending_dict[cid] = cCount
        print(trending_dict)
    #o.write(line)

i.close()
o.close()    