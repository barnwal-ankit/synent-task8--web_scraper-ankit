# synent-task8--web_scraper-ankit

# LCSC Table Downloader

A Python automation script that uses Playwright to download CSV tables from multiple pages on the LCSC website.

## Features

- Automates CSV downloads from LCSC product listings
- Saves each page as a separate CSV file
- Supports downloading multiple pages automatically
- Allows manual filter and page size selection before starting

## Requirements

- Python 3.x
- Playwright

Install Playwright:

```bash
pip install playwright
playwright install
```

## How to Run

1. Update the `URL` and `TOTAL_PAGES` variables if needed.
2. Run the script:

```bash
python lcsc.py
```

3. The browser will open.
4. Manually configure the desired filters and page size.
5. Press **Enter** in the terminal to begin downloading.
6. The CSV files will be saved in the `lcsc_downloads` folder.

## Output

Downloaded files are saved as:

```
lcsc_downloads/
├── page_001.csv
├── page_002.csv
├── page_003.csv
└── ...
```

## Notes

- The browser runs in non-headless mode to allow manual setup.
- Ensure your internet connection remains active during the download process.
- Adjust `TOTAL_PAGES` to match the number of pages you want to download.

## Author

Created as a Playwright automation project for downloading product table data from LCSC.
