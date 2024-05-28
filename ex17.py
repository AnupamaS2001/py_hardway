from sys import argv 
from os.path import exists

sript,from_file,to_file=argv
print(f"copying from {from_file} to {to_file}")
in_file=open(from_file)
indata=in_file.read()

print(f"The file is {len(indata)} bytes long")

print(f"Does the output file exists? {exists(to_file)}")
print(f"Ready, hit RETURN to continue, CTRL-C to abort")

input()

out_file=open(to_file, 'w')
out_file.write(indata)
print("Alright,all done")

out_file.close()
in_file.close()