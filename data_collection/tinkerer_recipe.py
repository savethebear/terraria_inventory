from bs4 import BeautifulSoup
import urllib.request
import json

class Item:
    def __init__(self, name, img_src, object_link):
        self.name = name
        self.img_src = img_src
        self.object_link = object_link

    def get_obj(self):
        return {
            'name': self.name,
            'img_src': self.img_src,
            'object_link': self.object_link
        }

    def get_str(self):
        return json.dumps(self.get_obj(), separators=(',', ':'))


MAIN_SITE = "https://terraria.gamepedia.com"

html_page = urllib.request.urlopen("https://terraria.gamepedia.com/Tinkerer%27s_Workshop")
soup = BeautifulSoup(html_page, 'lxml')

table = soup.find("div", class_='crafts').table.tbody
rows = table.find_all("tr")[1:]

with open("tinker_recipes.json", 'w') as f:
    output = []
    prev_result = None
    for row in rows:
        row_obj = {}

        # compute result
        result = row.find('td', class_="result")
        if result is None:
            result = prev_result
        else:
            result = result.a
            prev_result = result
        
        row_obj['result'] = Item(result['title'], result.img['src'], MAIN_SITE + result.get('href')).get_obj()

        # compute ingredients
        objects = []
        ingredients = row.find('td', class_="ingredients").find_all('li')
        for item in ingredients:
            details = item.span.a
            objects.append(
                Item(details['title'], details.img['src'], MAIN_SITE + details['href']).get_obj()
            )
        
        row_obj["ingredients"] = objects
        output.append(row_obj)

    json.dump(output, f)