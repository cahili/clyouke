# -*- coding: utf-8 -*-
# @Author: huerke
# @Date:   2016-09-03 23:53:58
# @Last Modified by:   Administrator
# @Last Modified time: 2016-09-05 09:17:07
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'mysql://root:qwer@localhost/caoliu'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
domain_name = 'http://t66y.com/'


class Crawler(object):
    def __init__(self, start_url):
        self.start_url = start_url

    def spider(self, url):
        r = requests.get(url)
        r.encoding = 'gbk'
        html_doc = r.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        return soup

    def get_dict(self):
        dc = {}
        for page in range(1, 100):
            url = self.start_url.format(page)
            soup = self.spider(url)
            h3 = soup.find_all('h3')
            for h3_ in h3:
                a = h3_.find_all('a', recursive=False)
                for a_ in a:
                    title = a_.get_text()
                    link = a_['href']
                    dc[title] = link
        return dc


class Jishuqu(db.Model):
    __tablename__ = 'jishuqu'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    link = db.Column(db.Text)

    def __repr__(self):
        return '<Jishuqu %r>' % self.title


class Dagaier(db.Model):
    __tablename__ = 'dagaier'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    link = db.Column(db.Text)

    def __repr__(self):
        return '<Dagaier %r>' % self.title


if __name__ == '__main__':
    db.create_all()
    url = domain_name + 'thread0806.php?fid=7&search=&page={}'
    s = Crawler(url)
    dc = s.get_dict()
    num = 1
    for (n, k) in dc.items():
        # print "key:" + n + ",value:" + str(k)

        # 根据查询结果判断是不是增加数据
        if (Jishuqu.query.filter(Jishuqu.title == n).first()):
            pass
        else:
            data = Jishuqu(title=n, link=k)
            db.session.add(data)
            db.session.commit()
            db.session.close()
            print '技术讨论区第{}次存储'.format(num)
            num = num + 1

    url = domain_name + 'thread0806.php?fid=16&search=&page={}'
    s = Crawler(url)
    dc = s.get_dict()
    num = 1
    for (n, k) in dc.items():

        # 根据查询结果判断是不是增加数据
        if (Dagaier.query.filter(Dagaier.title == n).first()):
            pass
        else:
            data = Dagaier(title=n, link=k)
            db.session.add(data)
            db.session.commit()
            db.session.close()
            print '达盖尔区第{}次存储'.format(num)
            num = num + 1
