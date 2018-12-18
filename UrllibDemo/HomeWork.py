#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request;
import json;
def fetch_data(url):
    req=request.Request(url);
    with request.urlopen(req) as f:
        return json.loads(f.read().decode("utf-8"))

URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data=fetch_data(URL);
#断言：通过继续，不通过报错
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')