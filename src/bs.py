from bs4 import BeautifulSoup
import requests

url = ''
headers = {
    'user-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'
}

try:
    response = requests.request(
        method= 'GET',
        url= url,
        headers=headers
    )
    print("request header:")
    for key, value in response.request.headers.items():
        print(f"{key}: {value}")

    print("\nresponse header:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all(
        name='',
        class_=''
    )

    for article in articles:
        print(article.text)

except requests.exceptions.RequestException as e:
    print("request error:", e)
except Exception as e:
    print("error:", e)
