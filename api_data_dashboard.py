
# this data dashboard will use data from an API to display 
# information regarding the crypto prices and plot interactive charts with matplotlib and plotly
import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

api_url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false"
def fetch_crypto_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    
def display_crypto_data(crypto_data):
    if not crypto_data:
        print("No data to display.")
        return
    print(f"{'Name':<20} {'Symbol':<10} {'Current Price (USD)':<20} {'Market Cap (USD)':<20}")
    print("="*70) 
    for coin in crypto_data:
        name = coin.get('name', 'N/A')
        symbol = coin.get('symbol', 'N/A').upper()
        current_price = coin.get('current_price', 0)
        market_cap = coin.get('market_cap', 0)
        print(f"{name:<20} {symbol:<10} ${current_price:<20,.2f} ${market_cap:<20,.2f}")


def crypto_currency(crypto_data, filename='crypto_prices.pdf'):
    if not crypto_data:
        print("No data to plot.")
        return
    df = pd.DataFrame(crypto_data)
    df.set_index('name', inplace=True)
    plt.title('Crypto currency Prices')
    x = df.index
    plt.figure(figsize=(12, 6))
    plt.xlabel('Cryptocurrency')
    plt.ylabel('Current Price (USD)')
    y = df['current_price']
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    
    
def market_cap(crypto_data, filename='market_cap.pdf'):
    if not crypto_data:
        print("No data to plot.")
        return
    df = pd.DataFrame(crypto_data)
    df.set_index('name', inplace=True)
    plt.figure(figsize=(12, 6))
    plt.title('Cryptocurrency Market Cap')
    plt.xlabel('Cryptocurrency')
    plt.ylabel('Market Cap (USD)')
    x = df.index
    y = df['market_cap']
    plt.bar(x, y, color='orange')
    
   
def make_pdf(crypto_data, filename='crypto_analytics.pdf'):
    with PdfPages(filename) as pdf:
        crypto_currency(crypto_data)
        plt.savefig(pdf, format='pdf')  
        market_cap(crypto_data)
        plt.savefig(pdf, format='pdf')

def main():
    crypto_data = fetch_crypto_data(api_url)
    display_crypto_data(crypto_data)
    df = pd.DataFrame(crypto_data)
    crypto_currency(crypto_data)
    market_cap(crypto_data)
    make_pdf(crypto_data)
   
if __name__ == "__main__":
    main()  