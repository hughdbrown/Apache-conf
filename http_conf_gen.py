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
eJyVU8Fu00AQvfsrBveQFhqnEhwQiiIiErWgEldN4YKQtbHH9lbeHWt23BBF/Dtrm0TBRULsafR2
3pu3M7NnoGqVlpgImrpSgpH8kGClDH7VLI2qbsgJvHz39ioIpkNoFoA/a+Qn5HlmtIUtboxygvx+
7zo4sV7qhft5ktmKw/C6u19Q2hi0ck8kEO4dNZxikmn2GZN9zfSIqRwok7AnTW8pVaLJQjgJe0ft
OYOtlpIaASm1u4QdNaOqggIF3ly9hhrZaOdaGjITuxPivOsIjCH8UGlvBzK0GjPY7KB3DSnZXBcN
d3VDOHJVVdEWcibThsERX6PcKJtVnlrvvCs79o8pWJljxl0HH5KyR2ULilJijMoec5GhrCcPSHHd
vf43h9vePWtWMOAscNMUEA+l7pSUEH4jF9U+iiyxaYNzdwE5MTjwIz7n0Z+TGV2Ch/rySZveYhfw
HV6B2/VK4WknlvYJFp/mq+s4WS8fHj6urtfJ53jx5XYJQ9uRQxFtCzfwOW+E7rEilUGc5/0aTA57
MHu+FwYzrUKY/W0gK7L4bwWnBcf/LTOdnHyZWfALJ+sU9A==
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
