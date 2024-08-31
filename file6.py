file1 = open("test.txt", "r")
file1 = open("test.txt")      # equivalent to 'r' or 'rt'
file1 = open("test.txt",'w')  # write in text mode
file1 = open("img.bmp",'r+b') # read and write in binary mode

# open a file
file1 = open("test.txt", "r")

# read the file
read_content = file1.read()
print(read_content)

# open a file
file1 = open("test.txt", "r")

# read the file
read_content = file1.read()
print(read_content)

# close the file
file1.close()

try:
    file1 = open("test.txt", "r")
    read_content = file1.read()
    print(read_content)

finally:
    # close the file
    file1.close()

with open("test.txt", "r") as file1:
    read_content = file1.read()
    print(read_content)

filename ='John.txt'
with open(filename) as f_obj:
    contents = f_obj.read()

filename = 'John.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file "+ filename + " does not exist."
    print(msg) # Sorry, the file John.txt does not exist.