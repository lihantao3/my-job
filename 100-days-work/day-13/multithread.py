from time import sleep, time
from random import randint
from threading import Thread


class DownloadTask(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成，耗时%d秒' % (self._filename, time_to_download))


def main():
    start = time()
    t1 = DownloadTask('文件1')
    t2 = DownloadTask('文件2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗时%.2f秒' % (end - start))


if __name__ == '__main__':
    main()
