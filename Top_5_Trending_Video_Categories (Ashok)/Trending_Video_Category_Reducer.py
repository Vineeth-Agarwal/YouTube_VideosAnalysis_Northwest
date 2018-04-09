i = open("sorteddata_category.txt","r")
o = open("CategoryCount_TopicWise.txt","w")

cID = ''
cName = ''
cCount = 0		 
for line in i:
	category_id = line
	if cID == "":
		cID = category_id
		cCount = 1
	else:    		
		if cID == category_id:
			cCount += 1
		else:
			o.write("Category id: "+ cID + "\t"+ str(cCount) +"\n")
			print("Category id: "+ cID + "\t"+ str(cCount) +"\n")
			cID = category_id			
			cCount = 1	
    			
i.close()
o.close()
