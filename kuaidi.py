#!/usr/bin/env python
# encoding: utf-8
import json
import requests
from flask import Flask, Response
from company_map import COMPANY_MAP

app = Flask(__name__)


@app.route('/')
def index():
    return u'''zhe shi 一个 shenqi de 网zhan! dai wo 们走近人jian de天堂。'''


@app.route('/<company>/<postid>')
def latest_post_info(company, postid):
    company = COMPANY_MAP.get(company.replace(" ", "").upper())
    if not company:
        return u'快递公司名称错误'
    url = "http://www.kuaidi100.com/query?type=%s&postid=%s"
    resp = requests.get(url % (company, postid))
    data = resp.json()
    return Response(json.dumps(data, ensure_ascii=False),
                    mimetype='application/json')

if __name__ == '__main__':
    app.run()
