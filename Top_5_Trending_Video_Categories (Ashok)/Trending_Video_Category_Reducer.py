i = open("sorteddata_category.txt","r")
o = open("final.txt","r+")


category = ""
categoryCount = 0		 

for line in i:
	data = line.strip().split("\t")
	category_name,category_id = data
	if category == "":
		category = category_name
		categoryCount = 1
	else:
		if category == category_name:
			categoryCount += 1
		elif category!=category_name:
				print (category +"\t"+ str(categoryCount))
				o.write(str(categoryCount) +"\t"+ category +"\n")
				category = category_name
				categoryCount = 1

i.close()
o.close()
