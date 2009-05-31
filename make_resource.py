from __future__ import with_statement

def encode_resource(resource_name, s) :
	format = '%s = """\n%s"""'
	t = s.encode("zlib").encode("base64")
	return format % (resource_name, t)

if __name__ == "__main__" :
	import sys
	for arg in sys.argv[1 : ] :
		with open(arg) as f :
			s = f.read()
			i = arg.index(".txt")
			resource_name = arg[ : i]
			print encode_resource(resource_name, s)
