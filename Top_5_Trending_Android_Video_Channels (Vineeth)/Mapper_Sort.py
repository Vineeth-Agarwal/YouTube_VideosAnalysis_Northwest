input=open("./Android_Channels_Mapper_Out.txt","r")
output=open("./Sort_OuNew1.txt","w")
arr = []

# reading mapper output into a list and then converting it into tuple and storing in a list
for line in input:
    data=line.strip().split("\t")
    one,two,three=data
    tup=(int(one),two,three)
    arr.append(tup)

# Sorting by views and storing into new list
newArr=(sorted(arr, key=lambda student: student[0]))
# Writingto output file
output.write("\n".join('%s, %s, %s' % x for x in newArr))

# Close input & output files
input.close()
output.close()

