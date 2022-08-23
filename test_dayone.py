import pytest
import requests

class Test_ceshi:

    access_token = ""

    def test_get(self):
        url = "https://api.weixin.qq.com/cgi-bin/token"
        data = {"grant_type": "client_credential",
                "appid": "wx6bllb3efdlcdc290",
                "secret": "l06a9c6157c4db5f6029918738f9529d"
                }
        rep = requests.get(url=url, params=data)
        print(rep.json())
        Test_ceshi.access_token = rep.json()['errcode']


# print(Test_ceshi.access_token)

    def test_posta(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/updata?access token=" + Test_ceshi.access_token + ""
        safa = {"tag": {"id": 123, "name": "zhaolin"}}
        rep = requests.post(url=url, json=safa)
        print(rep.json())

    def test_shangchuang(self):
        url="https://api.weixin.qq.com/cgi-bin/media/uploudimg?access_token="+Test_ceshi.access_token+""
        data={
            "media":open(r"D:\\112.jpeg","rb")
              }
        rep=requests.post(url=url,files=data)
        print(rep.json())


if __name__ == '__main__':
    pytest.main('-vs')

# url ="http://bcs-route-gateway-service.test.k8s.chj.cloud/ssp-vehicle-alarm-service/api/app-notice/v1-0/download-vin-import-template"
# data = {
#
#   "bizType": "configurator",
#   "cbDesc": "回调描述",
#   "cbOwner": "负责人",
#   "endpoint": "http://endpoint",
#   "operatedBy": "操作人",
#   "shortname": "xcu_log_config"
# }
# head={"X-CHJ-GWToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJlS3dBejJaOTFTcTdFQUw0YjBqV2preFJUWENuY01nSiJ9.8qyI8Z9dhZJbt61fgXIAUsg6hYAi1TClat1DefuA510"}
# aa=requests.post(url=url,data=data,headers=head)
# print(aa.json())
