import hashlib
import http
import json
import urllib

import requests

apikey = '61040ae1-97c1-400c-9857-5dff60e17368'
secretkey = 'FB615FFF85D061BD568A068E7CCB4B33'
url = 'https://www.okex.com/api/v1/future_order_info.do'


def buildMySign(params, secretKey):
    sign = ''
    for key in sorted(params.keys()):
        sign += key + '=' + str(params[key]) + '&'
    data = sign + 'secret_key=' + secretKey
    return hashlib.md5(data.encode("utf8")).hexdigest().upper()


parmas = {
    "api_key": "61040ae1-97c1-400c-9857-5dff60e17368"}


def future_orderinfo():
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
    }
    params = {
        'api_key': apikey,
        'symbol': "eos_usd",
        'contract_type': "this_week",
        'order_id': "-1",
        'status': "2",
        'current_page': "1",
        'page_length': "50",
    }
    params['sign'] = buildMySign(params, secretkey)
    response = requests.post(url=url, params=params, headers=headers)
    orderData = response.json()
    a = orderData


# future_orderinfo()
if __name__ == '__main__':
    print(buildMySign(parmas, "FB615FFF85D061BD568A068E7CCB4B33"))
