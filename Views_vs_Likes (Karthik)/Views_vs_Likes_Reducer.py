import math
i = open("sortedoutput.txt","r")
o = open("reduceroutput.txt","w")
count = 0
o.write("Video ID  Video Name  Views  Likes\n")
o.write("------------------------------------\n")
for line in i:
    if count<5:
        data = line.strip().split(',')
        ratio,video_key=data
        video_data = video_key.strip().split("++")
        video_id,video_name,views,likes = video_data
        o.write(video_id+"  "+video_name+"  "+str(int(round(float(views))))+"  "+str(int(round(float(likes))))+"\n")
        count += 1
o.write("The above are top 5 videos with most likeliness")
i.close()
o.close()