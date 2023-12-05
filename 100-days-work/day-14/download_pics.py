import requests
from threading import Thread


class DownloadHandler(Thread):
    def __init__(self, url):
        super().__init__()
        self._url = url

    def run(self) -> None:
        filename = self._url[self._url.rfind('/') + 1:]
        resp = requests.get(self._url)
        with open('D:\\download\\pics\\' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    # 通过requests模块的get函数获取网络资源
    # 下面的代码中使用了天行数据接口提供的网络API
    # 要使用该数据接口需要在天行数据的网站上注册
    # 然后用自己的Key替换掉下面代码的中APIKey即可
    resp = requests.get('http://api.tianapi.com/meinv/?key=7f51f329af984f539b4c6fc48491bb0e&num=10')
    # 将服务器返回的json数据进行解析
    # data_model = resp.json()
    url_list = [
        'http://www.horosama.com/api/img/phone/phone_1.jpg',
        'http://www.horosama.com/api/img/phone/phone_10.jpg',
        'http://www.horosama.com/api/img/phone/phone_11.jpg'
    ]
    for url in url_list:
        # 多线程下载图片
        DownloadHandler(url).start()


if __name__ == '__main__':
    main()
