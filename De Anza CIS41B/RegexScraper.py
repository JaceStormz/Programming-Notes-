# Gautam Rao
# 9/27/2026
# Python version 3.13

"""
RegexScraper.py

Purpose:
    Extract the table, rows, headers, and cells from the supplied Planets.html
    file using focused regular expressions.

"""

import re
from collections import defaultdict
from pathlib import Path


class RegexScraper:

    # (Regex.py lines 157-171)
    '''
    Receives the html_text as a parameter when object is initialized, then checks that html_text is a str(String),
    if not a str raises exception. else it stores the value in html_text then create defaultdict as a list.
    '''
    def __init__(self, html_text):
        if not isinstance(html_text, str):
            raise TypeError("html_text must be a string")

        self._html_text = html_text
        self._table_data = defaultdict(list)

        # (Regex.py lines 157-171)
        '''
        break down. r takes raw string, [^>]* matches zero or more characters that are not >,
        (.*?) defines a capture group that matches content between the table tags. Matches zero or more whitespace characters.
        Capture everything in the table finding the closing table tag
        '''
        self._table_re = re.compile(
            r"<table\b[^>]*>(.*?)</table\s*>",
            # ignore case and allows dot to match across new line characters
            re.IGNORECASE | re.DOTALL
        )

        # (Regex.py lines 174-199)
        # capture the content in the table row and allows whitespace.
        # focus on the content in a table row
        self._row_re = re.compile(
            r"<tr\b[^>]*>(.*?)</tr\s*>",
            re.IGNORECASE | re.DOTALL
        )

        # (Regex.py lines 157-171)
        # find either tags th or td opening tag, allow character except > capture its contents and 
        # then find the matching closing tag 
        # made table header and table data  
        self._cell_re = re.compile(
            r"<(th|td)\b[^>]*>(.*?)</\1\s*>",
            re.IGNORECASE | re.DOTALL
        )

        # Applying Regular Expressions / tag recognition
        # Store a compiled regular expression, followed by one or more characters not including >, 
        # followed by >, while compiling it with the DOTALL tag.
        self._inline_tag_re = re.compile(r"<[^>]+>", re.DOTALL)

    # (Regex.py lines 157-171)
    # defines ExtractTable, search object's in HTML text, raises an error if no match is found else returns the content captured
    
    def ExtractTable(self):
        match = self._table_re.search(self._html_text)
        if not match:
            raise ValueError("No table element was found in the supplied HTML")
        return match.group(1)

    # (Regex.py lines 174-199)
    # defines _ExtractRows searches HTML table and returns all matching rows
    def _ExtractRows(self, table_html):
        return self._row_re.findall(table_html)

    # (Regex.py lines 157-171)
    #defines _ExtractCells searches HTML rows and returns all matching cells
    def _ExtractCells(self, row_html):
        return self._cell_re.findall(row_html)

    # Applying Regular Expressions / tag recognition
    # Defines TrimText removes HTMLL tags removes the unwanted white space to single space

    def _TrimText(self, cell_html):
        no_tags = self._inline_tag_re.sub("", cell_html)
        return " ".join(no_tags.split()).strip()

    # (Regex.py lines 197-200)
    '''
    Define ParseTable, extract the table, rows and cells, identify and clean the headers and data,
    create unique keys for the headers, associate the data with those keys, handle missing or extra values, 
    store the completed results, and return the headers and results.
    '''
    def ParseTable(self):
        table_html = self.ExtractTable()
        rows = self._ExtractRows(table_html)
        if not rows:
            raise ValueError("The table element contains no rows")
        # creates empty lists for header and rows
        headers = []
        data_rows = []

        for row_html in rows:
            cells = self._ExtractCells(row_html)
            if not cells:
                continue
            # Get the cell
            tags = [tag.lower() for tag, _ in cells]
            # Clean the cell
            values = [self._TrimText(content) for _, content in cells]
            # Identify the header row
            if not headers and "th" in tags:
                headers = values
            else:
                data_rows.append(values)

        if not headers:
            raise ValueError("No header row containing <th> cells was found")
        
        keys = []
        seen = defaultdict(int)
        # Process every header
        for index, header in enumerate(headers, start=1):
            base = header if header else f"column_{index}"
            seen[base] += 1
            key = base if seen[base] == 1 else f"{base}_{seen[base]}"
            keys.append(key)
        # Create the results container
        results = defaultdict(list)
        for values in data_rows:
            # match values to key
            for index, key in enumerate(keys):
                value = values[index] if index < len(values) else ""
                results[key].append(value)
            # Extra value handler
            for index in range(len(keys), len(values)):
                results[f"cell_{index + 1}"].append(values[index])

        self._table_data = results
        return headers, results

    # DefaultDict.ipynb grouping / missing-key behavior
    # Defines GetColumn, looks up the specified key, and returns the values associated with that key as a list.
    def GetColumn(self, key):
        return list(self._table_data.get(key, []))

'''
Finally:
Python file is run directly, locates and reads Planets.html, create a RegexScraper using its HTML, 
Organizes the table into headers and data, print the headers, and then print each header with its column data.
'''
if __name__ == "__main__":
    
    html_path = Path(__file__).with_name("Planets.html")
    html = html_path.read_text(encoding="utf-8")

    scraper = RegexScraper(html)
    headers, data = scraper.ParseTable()

    print("Headers:")
    print(headers)
    print("\nExtracted columns:")
    for header in data:
        print(f"{header}: {data[header]}")

    # personal note to the professor: I added the short inline notes for myself so I can follow the logic later.
