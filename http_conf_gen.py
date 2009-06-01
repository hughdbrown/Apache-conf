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
eJytU8Fu00AQvfsrBhcpCTR2JXpAKIqISNSC2qRqChdA1sYe2xt5d6zdcUOU8u+s7SZKXRAH2NP4
7bw3b2fGJyBKEecYMaqyEIwB/2BvLhR+kYYrUVySZXj17u2Z54260NgDd5Zo7tFMEiU1bHClhGU0
73e2gSPtpF7Yn0eZtTh0r5v7KcWVQs23RAz+zlJlYowSaVxGuCsNrTHmPSX0W9LoimLBkjT4od86
qs8JbCTnVDFwLu0pbKnqFQVkyHB+9gZKNEpaW9PQGDL2iDhpOgJD8D8U0tmBBLXEBFZbaF1DTDqV
WWWauj4cuKIoaAOpIVWH3gFfIl8KnRSOWm6dKz10j8mMUIeMmwbeJyVroTMKYjIY5C1mA0VJS+6Q
FmXz+keOqXv3rFlehzPFVZXBoit1IzgH/yvZoHRRoMmoOujbAaRkwIIbcd/0nk6mdwoOastHdXqN
DeA7vAa7bZX8407M9D1MP03mF4toObu7+zi/WEbXi+nnqxl0bQcWmaXObMfnpGK6xYJEAos0bdcg
3O/B+PleKEyk8GH8u4HMSeOfBvhXYSsZh/9Lvf5+WuFacOwG8i3or8vsIZPpQ6mzwUv/H0s1smNv
FB790GPvF/WGQb4=
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
