@echo off
python http_conf_gen.py --project_name=my_proj --source_dir=c:\users\hughdbrown\documents\django\apache-conf --server_name=example.com --flavor=mod_wsgi
python http_conf_gen.py --project_name=my_proj --source_dir=c:\users\hughdbrown\documents\django\apache-conf --server_name=example.com --flavor=mod_python
