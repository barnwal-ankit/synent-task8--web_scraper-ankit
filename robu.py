import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

scraper = cloudscraper.create_scraper()

base_urls = {
# "Carbon": "https://robu.in/product-category/electronic-components/resistors/carbon-resistors/",
# "Current Sense": "https://robu.in/product-category/electronic-components/resistors/current-sense-resistors/",
"Film": "https://robu.in/product-category/electronic-components/resistors/film-resistors/",
# "Metal Oxide": "https://robu.in/product-category/electronic-components/resistors/metal-oxide-resistors/",
# "Networks": "https://robu.in/product-category/electronic-components/resistors/resistor-networks-arrays/",
# "Thermistor": "https://robu.in/product-category/electronic-components/resistors/thermistor/",
# "LDR": "https://robu.in/product-category/electronic-components/resistors/light-dependant-resistors-ldr/",
# "Varistor": "https://robu.in/product-category/electronic-components/resistors/varistor/",
# "Wirewound": "https://robu.in/product-category/electronic-components/resistors/wire-wound-resistor/",
# "Kits": "https://robu.in/product-category/electronic-components/resistors/through-hole-resistor/"
}

for subcat, base in base_urls.items():

    print(f"\n🚀 Starting Subcategory: {subcat}")
    data = []
    page = 71

    filename = f"robu_{subcat.lower().replace(' ', '_')}.csv"

    # ✅ If file exists, remove it (fresh run)
    if os.path.exists(filename):
        os.remove(filename)

    while True:
        url = f"{base}page/{page}/"
        print(f"🔍 Page {page}: {url}")

        r = scraper.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        products = soup.select("li.product")
        print(f"   → Found {len(products)} products")

        # STOP if no products
        if len(products) == 0:
            print("   ⚠️ No products → End of pages")
            break

        for p in products:
            name_tag = p.select_one("h2.woocommerce-loop-product__title")
            name = name_tag.text.strip() if name_tag else ""

            price_tag = p.select_one(".price")
            price = price_tag.text.strip() if price_tag else ""

            text = p.get_text()
            sku = ""
            if "SKU:" in text:
                sku = text.split("SKU:")[1].split("\n")[0].strip()

            stock = "Yes"
            if "out of stock" in text.lower():
                stock = "No"

            data.append([subcat, name, sku, price, stock])

        # ✅ SAVE EVERY 10 PAGES (APPEND MODE)
        if page % 10 == 0:
            df = pd.DataFrame(data, columns=[
                "Subcategory", "Product Name", "SKU", "Price", "In Stock"
            ])

            # write header only if file doesn't exist
            df.to_csv(
                filename,
                mode='a',
                header=not os.path.exists(filename),
                index=False
            )

            print(f"💾 Saved up to page {page} ({len(data)} rows appended)")

            data = []  # clear buffer

        # last page condition
        if len(products) < 48:
            print("   ✅ Last page reached")
            break

        page += 1
        time.sleep(1)

    # ✅ FINAL SAVE (remaining pages < 10)
    if data:
        df = pd.DataFrame(data, columns=[
            "Subcategory", "Product Name", "SKU", "Price", "In Stock"
        ])

        df.to_csv(
            filename,
            mode='a',
            header=not os.path.exists(filename),
            index=False
        )

        print(f"✅ Final save ({len(data)} rows appended)")

    print(f"🎯 Completed: {filename}")