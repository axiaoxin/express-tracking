#!/usr/bin/env python
# encoding: utf-8
import logging
import requests
from flask import Flask
from company_map import COMPANY_MAP

app = Flask(__name__)


@app.route('/<company>/<postid>')
def latest_post_info(company, postid):
    company = COMPANY_MAP.get(company.replace(" ", "").upper())
    if not company:
        return u'快递公司名称错误'
    url = "http://www.kuaidi100.com/query?type=%s&postid=%s"
    resp = requests.get(url % (company, postid))
    data = resp.json()
    if data['status'] == "200":
        data = data['data'][0]
        return u"%s-%s" % (data['time'], data['context'])
    else:
        logging.warning(data)
        return u'%s' % data['message'].split(u'：')[-1]

if __name__ == '__main__':
    app.run()
