'''required for run once'''
# import requests 
import json
from bs4 import BeautifulSoup as BS

# run once
'''
with open('output.html', 'w+') as f:
    r = requests.get('https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists/1-1000')
    data = r.text
    f.write(data)
    f.close()
'''

with open('output.html', 'r') as f:
    html_doc = f.read()
    f.close()

soup = BS(html_doc, 'html.parser')

chars = []
words = []

for character in soup.find_all(class_="Hans"):
    chars.append(character.a.string)

for word in soup.find_all(class_="Latn"):
    words.append(word.a.string)

chinese = {}

for i in range(len(words)):
    chinese[chars[i]] = words[i]

with open('output.json', 'w+') as f:
    contents = json.dumps(chinese, indent=2)
    f.write(contents)
    f.close()
# Hans = Simplified Chinese
# Latn = Pinyin
