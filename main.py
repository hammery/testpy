

import requests
import json
import time
import sys
import os


import base64

def send(text):

	id=os.environ["SCKEY3"]
	data = {
	   "chat_id": id,         # 对话id。若是频道则为“@channel_id”
	  "text": text
	      # 消息的解析模式
	}
	print(data)

	## headers中添加上content-type这个参数，指定为json格式
	headers = {'Content-Type': 'application/json'}


	url= os.environ["SCKEY1"]
	print(url)
	jsons=json.dumps(data)
	print(jsons)

	## post的时候，将data字典形式的参数用json包转换成json格式。
	r = requests.post(url=url, headers=headers, data=jsons)
	print(r.text)
	# print(data)

def getservers():
	url= os.environ["SCKEY4"]
	print(url)

	
	headers = {'Content-Type': 'text/plain; charset=utf-8',
	'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
	}

	r = requests.get(url=url, headers=headers)
	
	t=base64.b64decode(r.text).decode("utf-8")
	# print(t.split('\n'))
	sends=t.split('\n') 
	for j in range(1,len(sends)):
		print(sends[j])
		send(sends[j])



if __name__ == '__main__':

	getservers()
##123
###123
###123
###123
###123
###123
###123
###123
###123
###123
###123
###123
###123
###123
###123
###123
###123
###123
