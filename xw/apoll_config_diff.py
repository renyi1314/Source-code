#!/usr/bin/env python
# coding=utf-8

import requests
import json


class PyApolloClient(object):
    def __init__(self,
                 appid,
                 cluster,
                 env=APOLLO_ENV,
                 token=APOLLO_TOKEN,
                 server_url=APOLLO_URL,
                 namespace=APOLLO_NAMESPACE,
                 timeout=30):
        self.env = env
        self.server_url = server_url
        self.token = token
        self.appid = appid
        self.cluster = cluster
        self.timeout = timeout
        self.namespace = namespace
        self.headers = {
            'Authorization': self.token,
            'Content-Type': 'application/json;charset=UTF-8'
        }

    def grant_token(self):
        url = '{}/consumers/{}/assign-role?envs={}&type=AppRole'.format(
            self.server_url, self.token, self.env)
        # print("request_url " + url)
        resp = requests.post(url, data={"appId": self.appid})
        if resp.ok:
            print(self.token, " has permission on ", self.appid)
        else:
            print(self.token, " grant permission fail on ", self.appid)
            print('reason: ', json.loads(resp.text).get('message'))

    def get_current_kvs(self):
        url = '{}/openapi/v1/envs/{}/apps/{}/clusters/{}/namespaces'.format(
            self.server_url, self.env, self.appid, self.cluster)
        resp = requests.get(url, headers=self.headers)
        if resp.ok:
            d = {}
            for i in resp.json():
                for item_info in i['items']:
                    d[item_info['key']] = item_info['value']
            return d


if __name__ == "__main__":
    need_create = []
    need_modify = []
    need_nochange = []
    client1 = PyApolloClient(appid=APOLLO_APPID,
                             cluster=APOLLO_CLUSTER,
                             env=APOLLO_ENV,
                             namespace=APOLLO_NAMESPACE)
    print('----------------token 授权--------------------')
    client1.grant_token()
    print('----------------获取当前 kv 值--------------------')
    kvs = client1.get_current_kvs()
    print('----------------配置对比--------------------')
    for item in json.loads(json_items):
        if item['key'] not in kvs.keys():
            need_create.append(item)
        elif item['value'] != kvs[item['key']]:
            need_modify.append(item)
        else:
            need_nochange.append(item)

    print("本次新增配置: ", need_create)
    print("本次修改配置: ", need_modify)
    print("已存在、无需修改的配置: ", need_nochange)
