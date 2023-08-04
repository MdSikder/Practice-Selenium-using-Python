import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.ubuy.qa/en/")

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)

# Find all the product names and prices on the page
# product_names = []
# product_prices = []
# for product in soup.find_all('div', class_='plp__wrap-product'):
#     name = product.find('div', class_='plp__desc').find('a').text.strip()
#     price = product.find('span', class_='plp__price-now').text.strip()
#     product_names.append(name)
#     product_prices.append(price)
#
# return product_names, product_prices


# if __name__ == "__main__":
#     # URL of the Carrefour Qatar page
#     url = "https://www.ubuy.qa/en/category/cell-phones-accessories-2335752011"

# product_names, product_prices = scrape_carrefour_products(url)
#
# # Print all product names and prices
# for name, price in zip(product_names, product_prices):
#     print(f"Product: {name}\nPrice: {price}\n")
