# Open the input and output files
input=open("../data/USvideos.csv","r")
output=open("./Android_Channels_Mapper_Out.txt","w")
count=1

# Reading the input file containing the fields related to each video
for line in input:
    data=line.strip().split(",")

    # print length of fields description row
    if(count==1):
        count+=1
        print len(data)

    # If data is valid in a row, assign it in 11 variables as below
    if(len(data)==11):
            video_id,title,channel_title,category_id,tags,views,likes,dislikes,comment_total,thumbnail_link,date,=data

            # If the tag field had Android or android in it, write it to mapper output file.
            if tags.find("Android")==-1 and tags.find("android")==-1:
                continue
            else:
                # print("{0}\t{1}\t{2}\n".format(views,channel_title,tags))
                output.write("{0}\t{1}\t{2}\n".format(views,channel_title,tags))            

# closing files
input.close()
output.close()