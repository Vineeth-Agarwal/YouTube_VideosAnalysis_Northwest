# input=open("./Sort.txt","r")
input=open("./Android_Channels_Mapper_Out.txt","r")
output=open("./Sort_OuNew1.txt","w")
arr = []
for line in input:
    data=line.strip().split("\t")
    # print(data)
    one,two,three=data
    tup=(int(one),two,three)
    arr.append(tup)

# print(arr)    
    # output.write(video_id,title,channel_title)
newArr=(sorted(arr, key=lambda student: student[0]))
output.write("\n".join('%s, %s, %s' % x for x in newArr))
# for item in newArr:
    # output.write("%s\n" % item)

    
# print(newArr)
# output.write()
# # count=1

# print(sorted(lines,key=lambda student: student[-1]))
# # lines.sort()
# for line in lines:
# 	output.write(line)
input.close()
output.close()


student_tuples = [('john', 'A', 11),('jane', 'C', 12), ('dave', 'B', 10)]
# print(student_tuples[0:])
# print(sorted(student_tuples, key=lambda student: student[2]))
# print(student_tuples[0:])







# # input=open("./Sort.txt","r")
# # output=open("./Sort_Out1.txt","w")
# # count=1
# # lines = input.readlines()
# # sorted(lines)
# # # lines.sort()
# # for line in lines:
# # 	output.write(line)
# # input.close()
# # output.close()


# student_tuples = [('john', 'A', 11),('jane', 'C', 12), ('dave', 'B', 10)]
# print(student_tuples[0:])
# print(sorted(student_tuples, key=lambda student: student[2]))
# # print(student_tuples[0:])