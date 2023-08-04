import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_carrefour_products(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []
    product_elements = soup.find_all('div', class_='product-card')
    for product_element in product_elements:
        product_name = product_element.find('div', class_='product-title').text.strip()
        print(product_name)
        product_price = product_element.find('span', class_='price').text.strip()
        print(product_price)
        products.append({
            'Name': product_name,
            'Price': product_price,
        })

    return products


if __name__ == '__main__':
    url = 'https://www.carrefourqatar.com/mafqat/en/c/FQAT16660201'
    products_data = scrape_carrefour_products(url)

    # df = pd.DataFrame(products_data)
    # df.to_excel('carrefour_products.xlsx', index=False)
