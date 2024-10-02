import requests
from bs4 import BeautifulSoup


url = '#'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
response = requests.get(url, headers=headers)


if response.status_code == 200:

    soup = BeautifulSoup(response.content, 'html.parser')

    prices = soup.find_all('div', class_='showPrice')

    if not prices:
        print("No elements with the class 'showPrice' were found.")

    for price in prices:

        price_text = price.get_text(
            strip=True).replace('$', '').replace(',', '')

        try:
            price_numero = float(price_text)

            if price_numero < 10000:
                print(f'Offer: ${price_numero}')

        except ValueError:
            print(f"No se pudo convertir el price: {price_text}")

else:
    print(f"Error al acceder a la página. Código de estado: {
          response.status_code})")
