s = open("s.txt","r")   # open file, read-only
r = open("r.txt", "w")    # open file, write

thisKey = ""
thisValue = 0

for line in s:
  data = line.strip().split('\t')
  id, likes = data

  if id != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')
    # start over when changing keys  
    thisKey = id 
    thisValue = 0

  # apply the aggregation function
  thisValue += int(likes)


# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()