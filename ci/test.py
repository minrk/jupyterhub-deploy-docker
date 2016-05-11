#!/usr/bin/env python
import requests
import docker
from docker.utils import kwargs_from_env

d = docker.Client(**kwargs_from_env())
hub = d.containers(filters={'name': 'jupyterhub'})[0]

ip = '127.0.0.1'
port = 443
hub_url = 'https://{}:{}'.format(ip, port)

def test_hub():
    r = requests.get(hub_url, allow_redirects=False, verify=False)
    assert r.status_code == 302
    r = requests.get(hub_url + '/static/css/style.min.css', verify=False)
    assert r.status_code == 200
