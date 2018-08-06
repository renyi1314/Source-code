import urllib

import urllib3

url = 'https://movie.douban.com/top250'

res = urllib.request.urlopen(url)

print(res)
