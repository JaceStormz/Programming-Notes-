# Gautam Rao
# 10/06/2026
# Python Version 3.13

"""
gui.py

Purpose:
    Display the table extracted by BS4Scraper in a Tkinter GUI.

Source:
    Tkinter.py was used as the starting point for the GUI structure.
    BS4scraper.py supplies the scraped table data.
"""

# (Tkinter.py lines 10-14)
# Added pathlib.Path to locate Planets.html relative to gui.py.

import tkinter as tk
from tkinter import ttk, scrolledtext
from pathlib import Path
# Added the BS4Scraper cause main script runs the scraper and passes it the GUI.
from BS4scraper import BS4Scraper


# (Tkinter.py lines 18-28)
# Renamed TkinterShowcase to TableGUI 
# Added headers and data parameters to scrape table to be passed directly to GUI.
class TableGUI(ttk.Frame):
    """Tkinter GUI that displays a scraped table."""

    def __init__(self, master, headers, data):
        super().__init__(master)

        # (Tkinter.py lines 30-36)
        master.title("Scraped Planets Table")
        master.geometry("1100x750")

        self._headers = headers
        self._data = data

        # (Tkinter.py lines 141-157) 
        # The scraped table is inserted by _display_table().
        # wrap="none" is used so table columns remain aligned.
        self.text_box = scrolledtext.ScrolledText(self, wrap="none")
        self.text_box.pack(expand=True, fill="both", padx=10, pady=10)

        self._display_table()
        self.pack(expand=True, fill="both")


    def _display_table(self):
        """Format the scraped columns into readable rows and display them."""

        if not self._headers:
            self.text_box.insert(tk.END, "No table data was returned.")
            return

        # BS4scraper.py returns the table as headers plus a dictionary
        # of column lists. Convert those columns back into display rows.
        columns = [self._data.get(header, []) for header in self._headers]
        row_count = max((len(column) for column in columns), default=0)
        # reconstructs rows from column-based data.
        rows = []
        for row_index in range(row_count):
            row = []
            for column in columns:
                value = column[row_index] if row_index < len(column) else ""
                row.append(value)
            rows.append(row)

        # Calculate a width for each column for readable.
        widths = []
        for index, header in enumerate(self._headers):
            values = [str(row[index]) for row in rows]
            width = max([len(str(header))] + [len(value) for value in values])
            widths.append(width)
        # Formats the table header for display.
        header_line = " | ".join(
            str(header).ljust(width)
            for header, width in zip(self._headers, widths)
        )
        separator = "-+-".join("-" * width for width in widths)

        output = [header_line, separator]
        # Formats every row so that its columns align with the previously calculated column widths.
        for row in rows:
            output.append(
                " | ".join(
                    str(value).ljust(width)
                    for value, width in zip(row, widths)
                )
            )

        # (Tkinter.py line 157)
        # Display the completed table in the Tkinter text box and then make the text box read-only.
        self.text_box.insert(tk.END, "\n".join(output))
        self.text_box.configure(state="disabled")
# (Tkinter.py lines 425-435)
# Added the scraper setup before creating the GUI.
# The scraper reads Planets.html then ParseTable() returns headers and data. 
# Passes headers and data into TableGUI.
if __name__ == "__main__":
    
    html_path = Path(__file__).with_name("Planets.html")
    html = html_path.read_text(encoding="utf-8")

    # The scraper remains responsible for extracting the table.
    scraper = BS4Scraper(html)
    headers, data = scraper.ParseTable()

    # The main script creates the GUI, passes in the scraped result, and starts the Tkinter main loop.
    root = tk.Tk()
    TableGUI(root, headers, data)
    root.mainloop()