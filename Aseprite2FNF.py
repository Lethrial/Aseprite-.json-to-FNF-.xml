import json
INDENT = '  '

jsonInput = input("Please type the name of the .json you'd like to convert: ")
xmlName = jsonInput[:-5]+".xml"
jsonFile = open(jsonInput,"r")
jsonRead = jsonFile.read()
jsonPy = json.loads(jsonRead)

frames = list(jsonPy['frames'].keys())
frame_len = len(frames)
image = jsonPy['meta']['image']

with open(xmlName,"a") as xml:
  xml.write('<?xml version="1.0" encoding="utf-8"?>')
  xml.write('\n<TextureAtlas imagePath="'+image+'">')
  for f in range(frame_len):
    frameName = str(frames[f])
    x = jsonPy['frames'][frameName]['frame']['x']
    y = jsonPy['frames'][frameName]['frame']['y']
    w = jsonPy['frames'][frameName]['frame']['w']
    h = jsonPy['frames'][frameName]['frame']['h']
    xml.write('\n'+INDENT+'<SubTexture name="'+frameName+'" x="'+str(x)+'" y="'+str(y)+'" width="'+str(w)+'" height="'+str(h)+'"/>')
  xml.write('\n</TextureAtlas>')

print("Conversion complete! Your output file is "+xmlName+".")