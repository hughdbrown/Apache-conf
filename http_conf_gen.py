#!/usr/bin/env python
from __future__ import with_statement

import sys
import optparse

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

def replace_templates(templates, **args) :
    for template in templates :
        fileNameTemplate, template_uud_zlib = template
        fileName = replace_template(fileNameTemplate, **args)
        msg = "Writing '%s'" % (fileName, )
        print >> sys.stderr, msg
        with open(fileName, "w") as f :
            textTemplate = template_uud_zlib.decode("base64").decode("zlib")
            textExpansion = replace_template(textTemplate, **args)
            f.write(textExpansion)

def main() :
    mod_wsgi = """
eJx1js0KwjAQhO95iloP2sv6BB4EpSraHqp4EAmhCW2k3Q3Z+If47kbQo5dhWGb2m2HSk5Y3biyE
exC2d+RDQvxz/GAhooBToQXlnEE9Tp9MF18bqa0f8GuSZoIYDF6tJzyO5utZkZeyWux2qyKv5Lac
7zeL0SmZJk/n6WzqIFH1JlaBTQgWmwj5AvVZYUNQkzfQKtSd8QyffUJEemdrFSxhfPU3CIcqXy2V
xngZZ+INW6NPqA==
"""
    apache_mod_wsgi = """
eJyNkU+LwjAQxe/5FGO9CRqPIqVsQVAvXgp6LLGZ3R1pTJmkVin73bf/XIqXdQ5DmPfeL2EyBVWo
7BtTY3VauS9a+LsXB2XwSOxLle+s8zBbr5ZChK+jSEBTCfINOdaGrlDh2SjnkT9q143Ta4OauJ+R
s4XDq9zp4YYYM2/5AUHtbMkZppq40WVdsL002jMQQH95WyrPbQWfbE177EnyDxX17Dgn5UAa1KTk
v/jBF4yjjjzO382PzD2ka6dku08ypsIPzDceYvWi/ZdAhHK0/0j8AiSIlEs=
"""
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
    amp = [("{project_name!s}.vhost.python.conf", apache_mod_python)]
    amw = [("{project_name!s}.vhost.wsgi.conf", apache_mod_wsgi), ("{source_dir!s}/{project_name!s}/mod.wsgi", mod_wsgi)]
    flavors = { 'mod_python' : amp, 'mod_wsgi' : amw }

    parser = optparse.OptionParser()
    parser.add_option("--django_path", "-d", action='store', default=get_django_path())
    parser.add_option("--project_name", "-p", action='store')
    parser.add_option("--source_dir", "-s", action='store')
    parser.add_option("--server_name", "-v", action='store')
    parser.add_option("--flavor", "-f", action='store', type="choice", choices=flavors.keys())
    options, arguments = parser.parse_args()

    args = {"django_path":options.django_path, "source_dir":options.source_dir, "project_name":options.project_name, "server_name":options.server_name}
    flavor = options.flavor

    if flavor :
        templates = flavors[flavor]
    else :
        print "Must define template or flavor"
        sys.exit(1)

    if not all(args.values()) :
        print "Missing required arguments : ", [ k for k,v in args.items() if not v ]
        sys.exit(1)

    replace_templates(templates, **args)

if __name__ == "__main__" :
    main ()
