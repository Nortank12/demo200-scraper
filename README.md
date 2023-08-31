# About
This program scrapes all the comments from [this](https://demo200.5mp.eu/web.php?a=demo200&o=yDaKba7PGL) website. Since it doesn't limit the amount of recods per query, browsers usually freeze after just a few seconds of loading.

If you want to be able to browse the comments, this piece of code might give you a lift.

# Install
Install the depedencies:
```
pip install -r requirements.txt
```

# Usage
You can write the collected data to a JSON file:
```
scraper.py json
```

or an SQLite database:
```
scraper.py sqlite
```

For browsing the database, you can use the [SQLite Database Browser](https://sqlitebrowser.org/). It is open source and cross platform.