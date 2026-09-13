import requests
import re
import exrex
from tqdm import tqdm

url = "https://discord.com/%s"
index = requests.get(url % "/channels/@me").text

sheets = set(re.findall(r'"([^"]*.css)"', index))

script = re.search(r'"/assets/web[^\"]*\.js"', index).group()
webjs = requests.get(url % script[1:-1]).text

for fst, snd in re.findall(r'"(\w+)"===e\?""\+e\+"([^"]+\.css)"', webjs):
    sheets.add("/assets/" + fst + snd)

mapping = dict()
for id, hash in re.findall(r'([0-9]+):"(\w{16})"', webjs):
    if id not in mapping:
        mapping[id] = []
    mapping[id].append(hash)

for pattern in re.findall(r'\/\^([][0-9()|]+)\$\/.test\(e\)', webjs):
    for id in exrex.generate(pattern):
        for hash in mapping.get(id, []):
            sheets.add(f'/assets/{hash}.css')

with requests.Session() as s:
    with open('stylesheet.txt', 'w') as f:
        for sheet in tqdm(sheets):
            if (response := s.get(url % sheet)).status_code == 200:
                f.write(response.text)

