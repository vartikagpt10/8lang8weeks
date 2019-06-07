from sys import argv
script, filename = argv

txt = open(filename)
print(f"here is your file {filename}")
print(txt.read())

print("type the filaname again:", end = "  ")
file_name = input("> ")

txt_again = open(file_name)

print(open(file_name).read())