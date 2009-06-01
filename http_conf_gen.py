#!/usr/bin/env python
from __future__ import with_statement

"""
python http_conf_gen.py [args]
args =
--project_name=portfolio
--source_dir=c:/users/hughdbrown/django
--server_name=192.168.168.253
--flavor=mod_python
"""

def get_django_path() :
    import django
    return getattr(django, '__path__')[0]

def get_python_lib() :
    from distutils.sysconfig import get_python_lib
    return get_python_lib()

def read_template_file(filename) :
    with open(template_file) as f :
        return f.read()

def replace_template(format, **kw) :
    try :
        s = format.format(**kw)
    except Exception :
        s = format.replace("{", "%(").replace("!s}", ")s") % kw
    return s

def main() :
    apache_mod_python = """
eJytU8Fu2zAMvfsrOPWQdmvsAuthGIJgwRK0G7q4aLpdhsFQbNpWYYmGRDcNgv37ZLsJMnfDLtOJ
eOJ7fCKpE5C1TEtMGHVdScaQnzhYSo3flOVGVtfkGF6/f3cRBJMhNA3AnxXaR7SzTCsDG1xr6Rjt
h53r4MR4qVfu51FmKw7D6+5+Tmmj0fAdEYPYOWpsikmmrM+IdrWlB0x5T4lET5rcUCpZkQERid5R
e05go7ikhoFL5c5hS82oqqBAhsuLt1Cj1cq5lobWknVHxFnXERiD+FgpbwcyNAozWG+hdw0pmVwV
je3qCjhwZVXRBnJLug2DA75CvpYmqzy13npXZuwfU1ipDxm3HbxPyh6kKShMyWJY9pgLNWU9eUCK
6+71zxzb9u5Fs4IBZ47rpoB4KHUruQTxnVxY+yg0ZHUbnLozyMmCAz/iUzv6fTKjc/BQXz5p01vs
DH7AG3DbXkkcd2JhHmH+eba8ipPV4v7+0/JqlXyJ519vFjC0HTpkVqZwA5+zhukOK5IZxHner0G0
34Ppy73QmCkpYPqngSzJ4N8G+E9hpxjH/0t9Eh19sGnwC8URIaA=
"""
    apache_mod_wsgi = None
    flavors = { 'mod_python' : apache_mod_python, 'mod_wsgi' : apache_mod_wsgi }

    import sys
    import optparse
    parser = optparse.OptionParser()
    parser.add_option("--django_path", "-d", action='store', default=get_django_path())
    parser.add_option("--project_name", "-p", action='store')
    parser.add_option("--source_dir", "-s", action='store')
    parser.add_option("--server_name", "-v", action='store')
    parser.add_option("--template", "-t", action='store')
    parser.add_option("--flavor", "-f", action='store', type="choice", choices=flavors.keys())
    options, arguments = parser.parse_args()

    args = {"django_path":options.django_path, "source_dir":options.source_dir, "project_name":options.project_name, "server_name":options.server_name}
    template_file_name = options.template
    flavor = options.flavor
    if template_file_name :
        template_text = read_template_file(template_file_name)
    elif flavor :
        template_uud_zlib = flavors[flavor]
        template_text = template_uud_zlib.decode("base64").decode("zlib")
    else :
        print "Must define template or flavor"
        sys.exit(1)

    if not all(args.values()) :
        print "Missing required arguments : ", [ k for k,v in args.items() if not v ]
        sys.exit(1)

    print replace_template(template_text, **args)

if __name__ == "__main__" :
    main ()
