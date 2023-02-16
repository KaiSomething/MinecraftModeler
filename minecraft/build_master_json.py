import os
import json
from PIL import Image

data = {}

print(os.listdir())

for main_folder in ['atlases', 'blockstates', 'lang', 'models', 'particles']:
    data[main_folder] = {}
    if(main_folder == "models"):
        for sub_folder in ["block", "item"]:
            data[main_folder][sub_folder] = {}
            for file in os.listdir(f"{main_folder}/{sub_folder}"):
                if(".json" in file):
                    f = open(f"{main_folder}/{sub_folder}/{file}")
                    data[main_folder][sub_folder][file] = json.loads(f.read())
                    f.close()
    else:
        for file in os.listdir(main_folder):
            if(".json" in file):
                f = open(f"{main_folder}/{file}")
                data[main_folder][file] = json.loads(f.read())
                f.close()

data["textures"] = {}
for folder in ["block", "item"]:
    data["textures"][folder] = {}
    for file in os.listdir("textures/"+folder):
        if(not ".mcmeta" in file):
            img = Image.open(f"textures/{folder}/{file}")
            data["textures"][folder][file] = [img.width, img.height]

f = open("master_data.json", "w")
f.write(json.dumps(data))
f.close()