import sys
import os

if __name__ == "__main__":
	print(sys.argv)
	if len(sys.argv) < 2:
		print("Please set the zeppelin directory")
		exit(0)
	path = sys.argv[1]
	if not os.path.isdir(path):
		print("%s is not a valid directory" %path)
	
	f = open("E:/KMK/zeppelin/zeppelin-zengine/src/main/java/org/apache/zeppelin/notebook/Note.java", "rt")
	detected = False
	for line in f :
		tokens = line.strip().split()
		if len(tokens) < 3:
			detected = False
			continue
		if detected and (tokens[0].startswith("this.") or tokens[0] == 'return'):
			print(line)
			detected = False
		if tokens[0] == 'public':
			if tokens[1] == 'void' and tokens[2].startswith('set'):
				print(line)	
				detected = True
				continue
			if tokens[2].startswith('get'):
				print(line)
				detected = True
			
	f.close()