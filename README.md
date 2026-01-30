# DiVA_LLM_Conference_Cleaner

(


aw@katharsis-llm:~$ source venv/bin/activate
(venv) aw@katharsis-llm:~$ 

(venv) aw@katharsis-llm:~$ ls -lh kth_metadata.duckdb 
-rw-rw-r-- 1 aw aw 2.2G Jan 28 15:13 kth_metadata.duckdb

(venv) aw@katharsis-llm:~$ ls -l confmeta/
total 824
-rw-rw-r-- 1 aw aw    313 Jan  9 21:28 __init__.py
drwxrwxr-x 2 aw aw   4096 Jan 30 14:10 __pycache__
-rw-rw-r-- 1 aw aw    161 Jan  9 21:17 config.py
-rw-rw-r-- 1 aw aw    606 Jan  9 21:17 db_io.py
-rw-r--r-- 1 aw aw 750872 Jan  7 20:58 dblp_conference_series.csv
-rw-rw-r-- 1 aw aw    781 Jan 29 21:07 geonames_cities.py
-rw-rw-r-- 1 aw aw  12972 Jan 30 13:08 llm_parse.py
-rw-rw-r-- 1 aw aw   2768 Jan  9 21:19 llm_series.py
-rw-rw-r-- 1 aw aw   4310 Jan 10 11:40 pipeline.py
-rw-rw-r-- 1 aw aw  11116 Jan 30 13:59 regex_utils.py

(venv) aw@katharsis-llm:~$ ls -lh dblp/
total 4.6G
-rw-r--r-- 1 aw aw 2.1K Jan  7 20:40 extract_conference_series.py
-rw-r--r-- 1 aw aw 4.6G Jan  6 23:34 dblp.nt.gz

(venv) aw@katharsis-llm:~$ ls -lh geonames/
total 19M
-rw-rw-r-- 1 aw aw  14M Jan 29 03:22 cities5000.txt
-rw-rw-r-- 1 aw aw 5.0M Jan 29 02:29 cities5000.zip
