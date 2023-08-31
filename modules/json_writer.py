from json import dump

def write(parsed_data: list):
    "Writes the parsed data to the `demo200_db.json` file."
    for item in parsed_data:
        item["created"] = str(item["created"])
    
    dump({"comments": parsed_data}, open("demo200_db.json", "w"), indent=4)