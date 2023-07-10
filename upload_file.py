import requests

class YaUploader:
    url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    def __init__(self, token: str):
        self.token = token

    def get_upload_link(self):
        params = {'path': '/req111111.txt'}
        headers = {
            'Authorization': 'OAuth ' + self.token,

        }
        resp = requests.get(self.url, headers=headers, params=params)
        print(resp.json())

        return resp.json()['href']

    def upload_file(self,path_file):
        url = self.get_upload_link()
        with open(path_file, 'rb') as f:
             res = requests.put(url,files= {'file': f })
             print('file upload',res.status_code)


token = ''
path_file = 'C:/requests.txt'
a =YaUploader(token)
a.upload_file(path_file)


