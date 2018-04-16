i = open("CategoryCount_TopicWise.txt","r")
o = open("Top5Trending.txt","w")

tupples_array = []

cat_id_mapping = {2:'Autos & Vehicles',1:'Film & Animation',
                  10:'Music',15:'Pets & Animals',17:'Sports',
                 19:'Travel & Events',20:'Gaming',22:'People & Blogs',
                 23:'Comedy',24:'Entertainment',25:'News & Politics',
                 26:'Howto & Style',27:'Education',28:'Science & Technology',
                  29:'Nonprofits & Activism',43:'Shows'}

for line in i:
    data = line.strip().split(",")
    cCount, cCid = data
    c = int(cCid)
    for cid in cat_id_mapping.keys():
        if c == cid:
            tupple = (int(cCount),cat_id_mapping[c])
            tupples_array.append(tupple)

sorted_array = (sorted(tupples_array, key=lambda array_elements: array_elements[0], reverse=True))
print(sorted_array)
o.write("\n".join('%s, %s' % new_array_elements for new_array_elements in sorted_array))

i.close()
o.close()    