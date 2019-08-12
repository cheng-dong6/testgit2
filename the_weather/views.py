from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect,HttpResponse
import os
import json
import requests
import datetime

# Create your views here.
def index(request):
    if request.method == 'GET':
        if os.path.exists('6天气数据.json'):
            cache_data = json.load(open('6天气数据.json', 'r', encoding='utf-8'))
            datetime.datetime.now() - datetime.timedelta(hours=8) > datetime.datetime.strptime(cache_data['time'],'%Y-%m-%d %H:%M:%S')
        else:
            city_code_zhengzhou = 101180101
            url = f'http://t.weather.sojson.com/api/weather/city/{city_code_zhengzhou}'
            resp = requests.get(url=url)
            if resp.status_code == 200:
                resp_json = resp.text
                with open('6天气数据.json',mode='w',encoding='utf-8') as file:
                    file.write(resp_json)

        dict_obj = json.load(open('6天气数据.json','r',encoding='utf-8'))
        # 错误原因为json.load()返回类型为fp.read()：
        # json.load(open('文件','r'))
        # 里面的文件必须打开,不然就是字符串
        time = dict_obj['time']
        data = dict_obj['data']
        today_shidu = data['shidu']
        today_pm25 = data['pm25']
        today_quality = data['quality']
        today_wendu = data['wendu']
        today_ganmao = data['ganmao']
        yesterday_dict = data['yesterday']
        forecast_list = data['forecast']
        # print(forecast_list)
        context={
            'time' : time,
            'today_shidu':today_shidu,
            'today_pm25':today_pm25,
            'today_quality':today_quality,
            'today_wendu':today_wendu,
            'today_ganmao':today_ganmao,
            'yesterday_dict':yesterday_dict,
            'forecast_list':forecast_list
        }
        # print(context['forecast_list'])
        return render(request,'the_weather/index.html',context)
    elif request.method == 'POST':
        city = request.POST.get('city')
        if os.path.exists('天气数据'+city+'.json'):
            cache_data = json.load(open('天气数据'+city+'.json', 'r', encoding='utf-8'))
            datetime.datetime.now() - datetime.timedelta(hours=8) > datetime.datetime.strptime(cache_data['time'], '%Y-%m-%d %H:%M:%S')
        else:
            city_list = json.load(open('最新_city.json', 'r', encoding='utf-8'))
            for x in city_list:
                if city == x['city_name']:
                    city_number = x['city_code']
                    url = f'http://t.weather.sojson.com/api/weather/city/{city_number}'
                    print(url)
                    resp = requests.get(url=url)
                    if resp.status_code == 200:
                        resp_json = resp.text
                        with open('天气数据'+city+'.json', mode='w', encoding='utf-8') as file:
                            file.write(resp_json)
                            break

        # dict_obj = json.load(open('天气数据'+city+'.json', 'r', encoding='utf-8'))
        # time = dict_obj['time']
        # data = dict_obj['data']
        # today_shidu = data['shidu']
        # today_pm25 = data['pm25']
        # today_quality = data['quality']
        # today_wendu = data['wendu']
        # today_ganmao = data['ganmao']
        # yesterday_dict = data['yesterday']
        # forecast_list = data['forecast']
        # # print(forecast_list)
        # context = {
        #     'time': time,
        #     'today_shidu': today_shidu,
        #     'today_pm25': today_pm25,
        #     'today_quality': today_quality,
        #     'today_wendu': today_wendu,
        #     'today_ganmao': today_ganmao,
        #     'yesterday_dict': yesterday_dict,
        #     'forecast_list': forecast_list
        # }
        return render(request, 'the_weather/index.html', context={})