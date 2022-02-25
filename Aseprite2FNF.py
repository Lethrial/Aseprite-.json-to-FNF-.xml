import json
INDENT = '  '

jsonInput = input("Please type the name of the .json you'd like to convert: ")
xmlName = jsonInput[:-5]+".xml"
jsonFile = open(jsonInput,"r").read()
jsonPy = json.loads(jsonFile)
frames = list(jsonPy['frames'].keys())

with open(xmlName,"a") as xml:
  xml.write('<?xml version="1.0" encoding="utf-8"?>')
  xml.write('\n<TextureAtlas imagePath="'+jsonPy['meta']['image']+'">')
  for f in range(len(frames)):
    x = jsonPy['frames'][str(frames[f])]['frame']['x']
    y = jsonPy['frames'][str(frames[f])]['frame']['y']
    w = jsonPy['frames'][str(frames[f])]['frame']['w']
    h = jsonPy['frames'][str(frames[f])]['frame']['h']
    xml.write('\n'+INDENT+'<SubTexture name="'+str(frames[f])+'" x="'+str(x)+'" y="'+str(y)+'" width="'+str(w)+'" height="'+str(h)+'"/>')
  xml.write('\n</TextureAtlas>')

print("Conversion complete! Your output file is "+xmlName+".")
