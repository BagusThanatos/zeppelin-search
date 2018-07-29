import sys
import os
import datetime


def containsPublicSetterGetter(filename):
	detected = False
	with open(filename, 'rt') as f:
		for line in f :
			tokens = line.strip().split()
			if len(tokens) < 3:
				detected = False
				continue
			if detected and ((tokens[0].startswith("this.") and tokens[1] == '=') or tokens[0] == 'return'):
				print(line)
				return True
			else:
				detected = False

			if tokens[0] == 'public':
				if tokens[1] == 'void' and tokens[2].startswith('set'):
					detected = True
					continue
				if tokens[2].startswith('get'):
					print(line)
					detected = True
	return False		
			

if __name__ == "__main__":
	start = datetime.datetime.now()
	print(sys.argv)
	if len(sys.argv) < 2:
		print("Please set the zeppelin directory")
		exit(0)
	path = sys.argv[1]
	if not os.path.isdir(path):
		print("%s is not a valid directory" %path)
	
	count = 0
	totalfiles = 0
	for dirname, dirnames, filenames in os.walk(path):
#		print(dirnames)
#		print(dirname)
#		print(filenames)
		if '.git' in dirnames:
			dirnames.remove('.git')
		for filename in filenames:
			if 'java' in filename:
				totalfiles+=1
				if  containsPublicSetterGetter(os.path.join(dirname, filename)):
					#print(filename)
					count+=1
	time = datetime.datetime.now() - start
	print("Time spent: %s", str(time))
	print("Java Files with public setter/getter: %s", count)
	print("Java Files : %s", totalfiles)