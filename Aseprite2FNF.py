import json
INDENT = '  '

jsonInput = input("Please type the name of the .json you'd like to convert: ")
xmlName = jsonInput[:-5]+".xml"
jsonFile = open(jsonInput,"r").read()
jsonPy = json.loads(jsonFile)
frames = list(jsonPy['frames'].keys())

with open(xmlName,"w") as xml:
  xml.write('<?xml version="1.0" encoding="utf-8"?>')
  xml.write('\n<TextureAtlas imagePath="'+jsonPy['meta']['image']+'">')
  xml.write(f'\n{INDENT}<!-- Generated using Aseprite .json to FNF .xml: https://github.com/Lethrial/Aseprite-.json-to-FNF-.xml -->')
  for f in frames:
    x = jsonPy['frames'][str(f)]['frame']['x']
    y = jsonPy['frames'][str(f)]['frame']['y']
    w = jsonPy['frames'][str(f)]['frame']['w']
    h = jsonPy['frames'][str(f)]['frame']['h']
    xml.write(f'\n{INDENT}<SubTexture name="{str(f)}" x="{str(x)}" y="{str(y)}" width="{str(w)}" height="{str(h)}"/>')
  xml.write('\n</TextureAtlas>')

print("Conversion complete! Your output file is "+xmlName+".")
