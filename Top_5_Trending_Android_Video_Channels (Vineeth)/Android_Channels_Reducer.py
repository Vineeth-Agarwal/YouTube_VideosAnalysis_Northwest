
# Open reducer input and reducer output files
reducerIN = open("./Android_Channels_Reducer_in.txt", "r")
reducerOut = open("./Android_Channels_Reducer_out.txt", "w")
count = 0

# read the lines
lines = reducerIN.readlines()
# for top 5 views write each to output files and break the loop after 5 writes.
for line in lines:
    reducerOut.write(line)
    count=count + 1
    if(count == 5):
        break 
# close input and output files.
reducerIN.close()
reducerOut.close()