
# Open reducer input and reducer output files
reducerIN = open("./Android_Channels_Reducer_in.txt", "r")
reducerOut = open("./Android_Channels_Reducer_out.txt", "w")
count = 0
current_channel=""
new_channel=""

# read the lines
lines = reducerIN.readlines()
# for top 5 views write each to output files and break the loop after 5 writes.
for line in lines:
    data=line.strip().split("\t")
    print data
    views,current_channel,tags=data
    if(current_channel == new_channel):
        continue
    else:
        new_channel=current_channel
        reducerOut.write(line)
        count=count + 1
        if(count == 10):
            break
# close input and output files.
reducerIN.close()
reducerOut.close()