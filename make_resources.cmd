@echo off
python make_resource.py mod_wsgi.txt > variables.txt
python make_resource.py apache_mod_wsgi.txt >> variables.txt
python make_resource.py apache_mod_python.txt >> variables.txt
