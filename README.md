# Robu Product Scraper

A Python web scraping script that extracts product information from Robu product category pages and saves the data to CSV files.

## Features

- Scrapes product name, SKU, price, and stock status
- Supports multiple product subcategories
- Automatically navigates through paginated results
- Saves data incrementally to prevent data loss
- Exports results as CSV files

## Requirements

- Python 3.x
- Required libraries:
  - cloudscraper
  - beautifulsoup4
  - pandas

Install the dependencies:

```bash
pip install cloudscraper beautifulsoup4 pandas
```

## How to Run

1. Update the `base_urls` dictionary with the desired product categories.
2. Set the starting page number if required.
3. Run the script:

```bash
python robu.py
```

## Output

The scraped data is saved as CSV files in the current directory.

Example:

```
robu_film.csv
```

Each CSV contains the following columns:

- Subcategory
- Product Name
- SKU
- Price
- In Stock

## Notes

- The script pauses briefly between page requests to reduce server load.
- Data is written to the CSV file every 10 pages and again after the final page.
- If an output file already exists, it is replaced with a fresh file before scraping begins.

## Author

Created as a Python web scraping project for collecting product information from Robu product listings.
