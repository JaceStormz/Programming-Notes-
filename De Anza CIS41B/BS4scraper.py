# Gautam Rao
# 09/28/2026
# Python Version 3.13

"""
BS4scraper.py

Purpose:
    Build a BeautifulSoup version of the RegexScraper that extracts the same table information and follows the same column-naming rules.
"""

from collections import defaultdict
from pathlib import Path
from bs4 import BeautifulSoup


class BS4Scraper:


    # (Beautifulsoup.py lines 126-134)
    '''
    Initialize the object, verify that the HTML text is a string, create a BeautifulSoup object from 
    it using the HTML parser, and create an empty defaultdict for the table data.
    handles the exceptions all code is inside a class 
    '''
    def __init__(self, html_text):
        if not isinstance(html_text, str):
            raise TypeError("html_text must be a string")

        self._html_text = html_text
        self._soup = BeautifulSoup(html_text, "html.parser")
        self._table_data = defaultdict(list)

    # (Beautifulsoup.py lines 191-196)
    # Define ExtractTable, search the BeautifulSoup object for a table, raise an error if no table is found otherwise, return the table.
    def ExtractTable(self):
        table = self._soup.find("table")
        if table is None:
            raise ValueError("No table element was found in the supplied HTML")
        return table

    # (Beautifulsoup.py lines 206-213)
    # Define ExtractRows, find all rows and raise an error if no contents found and return the rows
    def ExtractRows(self, table):
        rows = table.find_all("tr")
        if not rows:
            raise ValueError("The table element contains no rows")
        return rows

    # (Beautifulsoup.py lines 206-213)
    # Define ExtractCells, find all cells in the header and data and return them
    def ExtractCells(self, row):
        return row.find_all(["th", "td"], recursive=False)

    # Safe Soup Creation / get_text() overview
    # Define _TrimText, gets text from cell, removes unnecessary whitespace, converts whitespace to single spaces, returns cleaned text.
    
    def _TrimText(self, cell):
        text = cell.get_text(separator="")
        return " ".join(text.split()).strip()

    # (Beautifulsoup notebook)
    # Defines ParseTable, extracts table and rows, extracts and cleans cells, identifies header row, 
    # separates headers from data rows, creates keys from headers, matches data to keys, handles missing or extra values, 
    # stores completed table data, returns headers and data.
    def ParseTable(self):
        table = self.ExtractTable()
        rows = self.ExtractRows(table)
        # creates empty lists for header and rows
        headers = []
        data_rows = []

        for row in rows:
            cells = self.ExtractCells(row)
            if not cells:
                continue
            # Clean the cell and header check
            values = [self._TrimText(cell) for cell in cells]
            has_header = any(cell.name == "th" for cell in cells)

            if not headers and has_header:
                headers = values
            else:
                data_rows.append(values)

        if not headers:
            raise ValueError("No header row containing <th> cells was found")

        keys = []
        seen = defaultdict(int)
        #goes through each header while keeping track of its position, starting at 1
        for index, header in enumerate(headers, start=1):
            base = header if header else f"column_{index}"
            seen[base] += 1
            key = base if seen[base] == 1 else f"{base}_{seen[base]}"
            keys.append(key)

        results = defaultdict(list)

        for values in data_rows:
            for index, key in enumerate(keys):
                value = values[index] if index < len(values) else ""
                results[key].append(value)
            # Handles extra values
            for index in range(len(keys), len(values)):
                results[f"cell_{index + 1}"].append(values[index])

        self._table_data = results
        return headers, results

    # defaultdict grouping / missing-key behavior
    # Defines GetColumn, looks up the specified key, and returns the values associated with that key as a list. 
    def GetColumn(self, key):
        return list(self._table_data.get(key, []))
'''
Locates and reads Planets.html, creates a BS4Scraper using HTML, organizes the table into headers and data.
Prints the headers and prints each header with its column data
'''

if __name__ == "__main__":
    html_path = Path(__file__).with_name("Planets.html")
    html = html_path.read_text(encoding="utf-8")

    scraper = BS4Scraper(html)
    headers, data = scraper.ParseTable()

    print("Headers:")
    print(headers)
    print("\nExtracted columns:")
    for header in data:
        print(f"{header}: {data[header]}")
