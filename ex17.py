from sys import argv
from os.path import exists

script, fromfile, tofile = argv

print(f"copying from {fromfile} to {tofile}")
indata = open(fromfile).read()

print(f"the input file is {len(indata)} bytes long")
print(f"does the output file exist? {exists(tofile)}")
print("blah blah blah")
input()

outfile = open(tofile,"w")
outfile.write(indata)

print("alright, all done!")

outfile.close()