#!/bin/env python
#-*- coding: utf-8 -*-
import requests
import xml.etree.ElementTree as ET
import tkinter
import pprint
import json

encoding = 'pL%2Fjz9KXiEexgNjdpb41H6KIpuSFV47r6eUGXShozUAXjDiuKfLLKeLRA9yzVUVapK9BuTsnU%2B4L%2FhDYAapaEg%3D%3D'
Decoding = 'pL/jz9KXiEexgNjdpb41H6KIpuSFV47r6eUGXShozUAXjDiuKfLLKeLRA9yzVUVapK9BuTsnU+4L/hDYAapaEg=='

url = 'http://apis.data.go.kr/1613000/SubwayInfoService/getKwrdFndSubwaySttnList'
params ={'serviceKey' : Decoding, 'pageNo' : '1', 'numOfRows' : '10', '_type' : 'xml', 'subwayStationName' : '정왕' }

response = requests.get(url, params=params)
# xml 내용
#print(response.text)
contents = response.text

# 데이터 결과값 예쁘게 출력해주는 코드
pp = pprint.PrettyPrinter(indent=4)
print(pp.pprint(contents))