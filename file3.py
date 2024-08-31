fo= open("test.txt", "r")

print(fo.read())
fo.close()
fo= open("test.txt", "r")
print(fo.read(10))
fo.close()
