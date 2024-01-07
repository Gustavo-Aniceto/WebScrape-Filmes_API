import requests
from bs4 import BeautifulSoup

url = "https://www.boxofficemojo.com/daily/2022/?sort=date&ref_=bo_rl_freelink"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

filmes = []
cards = soup.find_all("td", class_="a-text-left mojo-field-type-release mojo-cell-wide")

for card in cards:
    title_element = card.find("a", class_="a-link-normal")
    if title_element:
        title = title_element.text.strip()
        url = "https://www.boxofficemojo.com" + title_element["href"]
        filmes.append({
            "name": title,
            "url": url
        })

for filme in filmes:
    print(filme["name"])
    print(filme["url"])
    print("\n")
