from sys import argv
from time import time
from modules import reader

if argv[1] == "json":
    from modules import json_writer
elif argv[1] == "sqlite":
    from modules import db_writer
else:
    print("Correct usage:")
    print(" - JSON: scraper.py json")
    print(" -   DB: scraper.py sqlite")
    exit(1)

print("\n-- Demo200 Scraper --\n")
total_time = time()

print("[1/3] Scraping the website...")
start = time()
data = reader.scrape()
print(f"[1/3] Done! {round(time() - start, 2)} sec\n")

print("[2/3] Parsing the HTML data...")
start = time()
data = reader.parse(data, sorted=True)
print(f"[2/3] Done! {round(time() - start, 2)} sec\n")

if argv[1] == "json":
    print("[3/3] Dumping data to JSON...")
    start = time()
    json_writer.write(data)
    print(f"[3/3] Done! {round(time() - start, 2)} sec\n")
    print("Your file can be found next to this program, named 'demo200_db.json'\n")
else:
    print("[3/3] Writing data to DB...")
    start = time()
    db_writer.write(data)
    print(f"[3/3] Done! {round(time() - start, 2)} sec\n")
    print("Your file can be found next to this program, named 'demo200_db.sqlite3'\n")

print(f"Total processing time:\t{round(time() - total_time, 2)} sec")
print(f"Total data count:\t{len(data)}\n")