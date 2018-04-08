i = open("UScomments.csv", "r")   # open file, read-only
o = open("o.txt", "w")   # open file, write

for line in i:
  #It splits the each line of code by ,
  data = line.strip().split(',')
  #Checks whether there are 4 parts
  if (len(data) == 4):
    id, text, likes, replies = data
    o.write(id + "\t" + likes+ "\n")

i.close()
o.close()