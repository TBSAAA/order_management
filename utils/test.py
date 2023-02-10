#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from time import localtime, time
from datetime import datetime, date
import random
from requests import get
from config import config
from notes import notes

if config.autoday == 'Y':
    import time as t
    import schedule


# 获取天气信息
def get_weather():
    # 天气城市id
    city_id = config.cityid
    # 毫秒级时间戳
    t = (int(round(time() * 1000)))
    headers = {
        "Referer": "http://www.weather.com.cn/weather1d/{}.shtml".format(city_id),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    url = "http://d1.weather.com.cn/dingzhi/{}.html?_={}".format(city_id, t)
    response = get(url, headers=headers)
    response.encoding = "utf-8"
    response_data = response.text.split(";")[0].split("=")[-1]
    response_json = eval(response_data)
    # print(response_json)
    weatherinfo = response_json["weatherinfo"]
    # 天气
    weather = weatherinfo["weather"]
    # 最高气温
    temp = weatherinfo["temp"]
    # 最低气温
    tempn = weatherinfo["tempn"]
    return weather, temp, tempn

# 获取日期信息、每日软文


def makedata():
    week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    year = localtime().tm_year
    month = localtime().tm_mon
    day = localtime().tm_mday
    today = datetime.date(datetime(year=year, month=month, day=day))
    print(today.isoweekday())
    week = week_list[today.isoweekday()-1]
    nowdate = "{} {}".format(today, week)
    # 获取在一起的日子的日期格式
    love_year = int(config.love_date.split("-")[0])
    love_month = int(config.love_date.split("-")[1])
    love_day = int(config.love_date.split("-")[2])
    love_date = date(love_year, love_month, love_day)
    # 获取在一起的日期差
    love_days = str(today.__sub__(love_date)).split(" ")[0]
    # 软文

    return love_days, nowdate


def postwechat(corpid, corpsecret, url='https://blog.csdn.net/obliv/article/details/127975916'):
    # 日期信息
    love_days, nowdate = makedata()
    # 天气信息
    weather, temp, tempn = get_weather()
    # 软文
    notedetail = str(random.choice(notes))
    # 请求头
    HEADERS = {"Content-Type": "application/json ;charset=utf-8"}
    # 获取token
    r = requests.get(
        f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}').text
    js = json.loads(r)
    token = js['access_token']
    # 获取图片链接
    try:

        files = {"files": open(config.files_path, "rb")}

        response = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token={token}&type=image',
                                 files=files)
        a = json.loads(response.text)
        media_id = a["media_id"]

    except:
        print('图片地址错误，检查后更改再运行')

    # data 中agentid 按应用实际id更换
    data = {

        "touser": "@all",
        "msgtype": "mpnews",
        "agentid": config.AgentId,
        "mpnews": {
            "articles":  [
                {
                    "title": config.title + nowdate+"\n\n",
                    "digest": config.cont1+"\n\n"+config.cont2 + "\n\n"+config.cont3+weather + "\n" + config.cont4 + "\n\n" + config.cont5+temp + "\n"+config.cont6+tempn + "\n\n"+config.cont7+"\n\n"+config.cont8+"\n"+config.cont9 + love_days + "天"+"\n" + config.cont10+"\n\n" + " 🍻"+notedetail,
                    "thumb_media_id": media_id,
                    "content_source_url": url,
                    "content": 'https://blog.csdn.net/obliv/article/details/127975916'+'\n'+'点击阅读原文查看精彩↓↓↓',
                }
            ]
        },
        "enable_id_trans": 0,
        "enable_duplicate_check": 0,
        "duplicate_check_interval": 1800
    }
    String_textMsg = json.dumps(data)
    # 企业微信应用地址
    wechaturl = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={token}'
    res = requests.post(wechaturl, data=String_textMsg, headers=HEADERS)
    print(res.text)
    re = json.loads(res.text)
    if re["errcode"] == 0:
        print('任务发送成功')

    else:
        print('任务发送失败，请根据返回鼓掌链接判断处理')


if __name__ == '__main__':
    if config.autoday == 'Y':

        try:
            schedule.every().day.at(config.autotime).do(
                postwechat, config.CORPID, config.COPRSECRET)
            print("定时任务已开启每日"+config.autotime + '进行任务发送')
        except:
            schedule.every().day.at('07:00').do(
                postwechat, config.CORPID, config.COPRSECRET)
            print("定时任务已开启每日"+config.autotime + '进行任务发送')

        while True:
            schedule.run_pending()
            t.sleep(30)
    else:
        # 手动推送
        postwechat(config.CORPID, config.COPRSECRET)
