i = open("UScomments.csv", "r")
o = open("o.txt", "w")

for line in i:
  data = line.strip().split(',')
  if (len(data) == 4):
    id, text, likes, replies = data
    o.write(id + "\t" + likes+ "\n")

i.close()
o.close()