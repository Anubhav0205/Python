fo= open("foo.txt","w")
fo.write("Techno Idia University\n")
fo.write("West Bengal")
fo.close()
fo= open("foo.txt","r")

for each in fo:
    print(each)
fo.close()
