import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('Length of index.html:', len(html))
suspect = ['AI-powered', 'revolutionize', 'seamless', 'game-changing', 'cutting-edge', 'state of the art', 'beacon', 'testament', 'tapestry']
for s in suspect:
    matches = len(re.findall(re.escape(s), html, re.I))
    if matches > 0:
        print(f'Found {matches} matches of "{s}"')
