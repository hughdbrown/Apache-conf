from __future__ import with_statement

def encode_resource(resource_name, s) :
	format = '%s = """\n%s"""'
	t = s.encode("zlib").encode("base64")
	return format % (resource_name, t)

if __name__ == "__main__" :
	import sys
	import glob

	write_file_name = "variable"
	with open(write_file_name, "w") as variable_file :
		msg = "Writing '%s'" % (write_file_name, )
		print >> sys.stderr, msg
		for arg in glob.glob("*.txt")  :
			with open(arg) as f :
				msg = "\tAdding '%s'" % (arg, )
				print >> sys.stderr, msg
				s = f.read()
				i = arg.index(".txt")
				resource_name = arg[ : i]
				variable_file.write(encode_resource(resource_name, s))

