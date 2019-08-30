import requests
from bs4 import BeautifulSoup


# Define url and credential information here
url = 'https://www.amazon.com/Sony-Mirrorless-Digital-28-70mm-ILCE7M3K/dp/B07RGXR19X/ref=sr_1_1_sspa?keywords=sony+a7&qid=1567177571&s=gateway&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzQjRSUVAwTkRET0hVJmVuY3J5cHRlZElkPUEwNDI3MzcxMTdLOENSNjU2WlRHRyZlbmNyeXB0ZWRBZElkPUEwNTIyNDMwNzYzSjEySUFUT1dGJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'}


page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')