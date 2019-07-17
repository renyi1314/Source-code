#!/usr/bin/env python
# coding=utf-8

import requests
import json
import datetime


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
        login_url = '{}/signin'.format(self.server_url)
        r = requests.get(login_url, auth=(APOLLO_USER, APOLLO_PASSWD), allow_redirects=False)
        if r.ok:
            login_cookie = r.cookies.get_dict()
            for key, value in login_cookie.items():
                self.headers['Cookie'] = '='.join([key, value])
        else:
            print("get cookie error")

        url = '{}/consumers/{}/assign-role'.format(self.server_url, self.token)
        params = {'type': 'AppRole'}
        data = {'appId': self.appid}
        resp = requests.post(url, params=params, headers=self.headers, data=json.dumps(data))
        if resp.ok:
            print(self.token, " has permission on ", self.appid)
        else:
            print(self.token, " grant permission fail on ", self.appid)
            print('reason: ', json.loads(resp.text).get('message'))

    def create_item(self, data):
        url = '{}/openapi/v1/envs/{}/apps/{}/clusters/{}/namespaces/application/items'.format(
            self.server_url, self.env, self.appid, self.cluster)
        resp = requests.post(url, headers=self.headers, data=json.dumps(data))
        if resp.ok:
            print(data, "create success")
        else:
            print(json.loads(resp.text))
            print('item create failed, reason: ',
                  json.loads(resp.text).get('message'))

    def modify_item(self, data):
        item_key = data['key']
        url = '{}/openapi/v1/envs/{}/apps/{}/clusters/{}/namespaces/{}/items/{}'.format(
            self.server_url, self.env, self.appid, self.cluster,
            self.namespace, item_key)
        resp = requests.put(url, headers=self.headers, data=json.dumps(data))
        if resp.ok:
            print(data, "modify success")
        else:
            print(json.loads(resp.text))
            print('modify item failed, reason: ',
                  json.loads(resp.text).get('message'))

    def publish_release(self, release_info):
        url = '{}/openapi/v1/envs/{}/apps/{}/clusters/{}/namespaces/application/releases'.format(
            self.server_url, self.env, self.appid, self.cluster)
        resp = requests.post(url,
                             data=json.dumps(release_info),
                             headers=self.headers)
        if resp.ok:
            print("publish success")
        else:
            print("publish failed, reason: ", resp.text)


if __name__ == '__main__':
    print('----------------变更授权--------------------')
    client2 = PyApolloClient(appid=APOLLO_APPID,
                             cluster=APOLLO_CLUSTER,
                             env=APOLLO_ENV,
                             namespace=APOLLO_NAMESPACE)
    client2.grant_token()

    if need_create:
        for item in json.loads(need_create):
            item['dataChangeCreatedBy'] = APOLLO_USER
            client2.create_item(item)

    if need_modify:
        for item in json.loads(need_modify):
            item['dataChangeLastModifiedBy'] = APOLLO_USER
            client2.modify_item(item)
        print('----------------发布配置--------------------')
    release_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    release_info = {
        "releaseTitle": "automation-release-" + release_time,
        "releaseComment": RL_COMMENT,
        "releasedBy": APOLLO_USER,
    }
    client2.publish_release(release_info)
