import math
i = open("sortedoutput.txt","r")
o = open("reducer_report_output.csv","w")
o.write("Video Name,Views,Likes\n")
for line in i:
        data = line.strip().split(',')
        ratio,video_key=data
        video_data = video_key.strip().split("++")
        video_id,video_name,views,likes = video_data
        o.write(video_name+","+str(int(round(float(views))))+","+str(int(round(float(likes))))+"\n")
        # print(video_name+","+str(int(round(float(views))))+","+str(int(round(float(likes))))+"\n")
i.close()
o.close()