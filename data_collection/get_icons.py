import os
import json
import time

def underscore_space(text):
    text = text.replace(" ", "_")
    text = text.replace("\'", "")
    return text

def curl(link, save_dir, name):
    os.system("(cd {} && curl {} >> {})".format(save_dir, link, underscore_space(name) + ".png"))

file_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = file_dir + "/../src/data/"
save_dir = file_dir + "/item_icons/"

source_file = data_dir + "tinker_recipes.json"

with open(source_file) as f:
    data = json.load(f)

downloaded_set = set()
for item in data:
    result = item["result"]
    result_name = result["name"]
    if result_name not in downloaded_set:
        downloaded_set.add(result_name)
        curl(result["img_src"], save_dir, result_name)
        time.sleep(1)
    
    for ingredient in item["ingredients"]:
        name = ingredient["name"]
        if name not in downloaded_set:
            downloaded_set.add(name)
            curl(ingredient["img_src"], save_dir, name)
            time.sleep(1)
