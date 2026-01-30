# confmeta/geonames_cities.py
import csv
from pathlib import Path

def load_city_country(path: str):
    """
    Load GeoNames cities file and return:
    {normalized_city_name: set([country_code, ...])}
    Uses 'asciiname' and ISO-2 country code.
    """
    path = Path(path).expanduser()
    city_map = {}

    with path.open(encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if len(row) < 9:
                continue
            asciiname = row[1].strip()   # asciiname
            country = row[8].strip()     # ISO-2 country code
            if not asciiname or not country:
                continue
            key = asciiname.lower()
            city_map.setdefault(key, set()).add(country)

    return city_map

