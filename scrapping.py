import requests
from bs4 import BeautifulSoup
import re
import locale

# configure your coin format about your country
locale.setlocale(locale.LC_ALL, 'es_AR.UTF-8')

url = ''  # you have to insert here your URL
precios = []  # array to save prices

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    # in "prices" we filter the content to search "span" with the class "currency_price" so you can modify it for your page.
    prices = soup.find_all('span', class_='currency_price')

    if not prices:
        print("No elements with the class 'currency_price' were found.")

    for price in prices:
        price_text = price.get_text(strip=True)

        price_text_cleaned = re.sub(r'[^\d,]', '', price_text)
        price_text_cleaned = price_text_cleaned.replace(
            ',', '.')

        try:
            price_numero = float(price_text_cleaned)
            # in precio_a_buscar you have to write the maxi amount of money you want to seek
            precio_a_buscar = 69000
            if price_numero < precio_a_buscar:
                precios.append(price_numero)
            else:
                print(f"No hay precios menores a {precio_a_buscar}")

        except ValueError:

            print(f"No se pudo convertir el price: '{price_text_cleaned}'")

    precios.sort(reverse=True)

    for precio in precios:
        print(f'Offer: {locale.currency(precio, grouping=True)}')

else:
    print(f"Error al acceder a la página. Código de estado: {
          response.status_code}")
