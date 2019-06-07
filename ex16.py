from sys import argv
script, filename = argv

print(f"we are going to erase {filename}.")
print("if you don't want that, hit control c.")
print("if you do want that hit return")

input("> ")

print("opening the file...")
target = open(filename, 'w')

print("truncating the file.  byeeee!")
target.truncate()

print("write 2 lines")

l1 = input("1 : ")
l2 = input("2 : ")

print("i am going to write these to the file")

target.write(l1)
target.write("\n")
target.write(l2)

print("finally, byeee")
target.close