# _*_ coding:utf-8 _*_
import os,sys,json
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import requests
import urllib3
urllib3.disable_warnings()
class SendRequests():
    def sendRequests(self,apiData):
        """
        发送接口请求
        :param apiData:接口请求数据
        :return: 返回接口响应信息，以json格式
        """
        try:
            # 发送请求数据
            method = apiData["method"]
            url = apiData["url"]
            if apiData["params"] == "":
                par = None
            else:
                par = eval(apiData["params"])
            if apiData["headers"] == "":
                h = None
            else:
                h = eval(apiData["headers"])
            if apiData["body"] == "":
                body_data = None
            else:
                body_data = eval(apiData["body"])

            type = apiData["type"]
            v = False
            if type == "data":
                body = body_data
            elif type == "json":
                body =json.dumps(body_data)
            else:
                body = body_data
            re =requests.request(method=method,url =url, headers =h,params = par,data = body,verify = v)
            msg = json.loads(re.text)
            msg['status_code']=re.status_code
            return msg

        except Exception as e:
            print(e)