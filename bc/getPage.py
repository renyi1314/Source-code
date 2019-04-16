import requests

UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"

url = "https://www.cj0599.com/lotteryV3/trend.do?lotCode=WFC"

params = {"user-agent": UserAgent}

response = requests.get(url, params=params)


a = response
