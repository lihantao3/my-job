#模拟时钟

from time import sleep


class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show_time(self):
        print(f'{self._hour}:{self._minute}:{self._second}')



def main():
    clock = Clock(hour=23, minute=59, second=59)
    while True:
        clock.run()
        sleep(1)
        clock.show_time()


if  __name__ == '__main__':
    main()
