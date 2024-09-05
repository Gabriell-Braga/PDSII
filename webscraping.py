import requests
from bs4 import BeautifulSoup
from database import get_db
from model import Model_Menu

def scrape_ufu_categorias():
    url = "https://ufu.br/graduacao"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    categorias = []

    for item in soup.select("#block-menu-block-2 ul.menu li.leaf a"):
        menuNav = item.get_text()
        link = "https://ufu.br"+item['href']
        categorias.append({"menuNav": menuNav, "link": link})

    return categorias

def save_to_db(categorias):
    db = next(get_db())

    for categoria in categorias:
        nova_categoria = Model_Menu(
            menuNav=categoria["menuNav"],
            link=categoria["link"]
        )
        db.add(nova_categoria)
    
    db.commit()
    db.close()

if __name__ == "__main__":
    categorias = scrape_ufu_categorias() 
    save_to_db(categorias)
