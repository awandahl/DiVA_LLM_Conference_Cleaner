# DiVA_LLM_Conference_Cleaner


```

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

(venv) aw@katharsis-llm:~$ python -m confmeta.pipeline
Fetched 200 conference rows for parsing

=== 1/200 PID 455472 name_seq 3 ===
RAW: 2011 IEEE International Conference on Communications, ICC 2011. Kyoto. 5 June 2011 - 9 June 2011
LLM output (streaming):
{
  "conf_name": "2011 IEEE International Conference on Communications, ICC 2011",
  "conf_place": "Kyoto",
  "conf_dates": "2011-06-05 / 2011-06-09",
  "note": "Extracted conference name with year; kept city and date range."
}

PARSED: name='2011 IEEE International Conference on Communications, ICC 2011' | place='Kyoto, JP' | dates='2011-06-05 / 2011-06-09' | order=199
NOTE: Extracted conference name with year; kept city and date range.
DBLP: lookup disabled




=== 2/200 PID 896668 name_seq 7 ===
RAW: Transducers 2015, Anchorage, Alaska, USA, June 21-25, 2015
LLM output (streaming):
{
  "conf_name": "Transducers 2015",
  "conf_place": "Anchorage, Alaska, USA",
  "conf_dates": "2015-06-21 / 2015-06-25",
  "note": "Extracted conference name and dates from the string; kept city, country, and date range as is."
}

PARSED: name='Transducers 2015' | place='Anchorage, Alaska, USA' | dates='2015-06-21 / 2015-06-25' | order=None
NOTE: Extracted conference name and dates from the string; kept city, country, and date range as is.
DBLP: lookup disabled




=== 3/200 PID 1659075 name_seq 4 ===
RAW: 47th IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), MAY 23-27, 2022, Singapore, Singapore
LLM output (streaming):
{
  "conf_name": "47th IEEE International Conference on Acoustics, Speech and Signal Processing, ICASSP",
  "conf_place": "Singapore, Singapore",
  "conf_dates": "2022-05-23 / 2022-05-27",
  "note": "Extracted acronym+year in name; separated city and country for place."
}

PARSED: name='47th IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), ICASSP' | place='Singapore, Singapore' | dates='2022-05-23 / 2022-05-27' | order=47
NOTE: Extracted acronym+year in name; separated city and country for place.
DBLP: lookup disabled




=== 4/200 PID 429014 name_seq 3 ===
RAW: the 6th ACM workshop on Formal methods in security engineering
PARSED: name='The 6th ACM Workshop on Formal Methods in Security Engineering' | place='' | dates='' | order=6
NOTE: no date detected or skipped by heuristic
DBLP: lookup disabled



```
