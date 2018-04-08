s = open("s.txt","r")
r = open("r.txt", "w")

thisKey = ""
thisValue = 0

for line in s:
  data = line.strip().split('\t')
  id, likes = data

  if id != thisKey:
    if thisKey:
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    thisKey = id 
    thisValue = 0

  thisValue += int(likes)



r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()