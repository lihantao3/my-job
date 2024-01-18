"""
多线程程序如果没有竞争资源处理起来通常也比较简单
当多个线程竞争临界资源的时候如果缺乏必要的保护措施就会导致数据错乱
说明：临界资源就是被多个线程竞争的资源
"""

import time
import threading
from random import randint
from concurrent.futures import ThreadPoolExecutor



class Account(object):
    """银行账户"""
    def __init__(self):
        self._balance = 0.0
        lock = threading.Lock()
        self._condition = threading.Condition(lock)

    def deposit(self, money):
        #通过锁保护临界资源
        with self._condition:
            new_balance = self._balance + money
            time.sleep(0.001)
            self._balance = new_balance
            self._condition.notify_all()

    def withdraw(self, money):
        with self._condition:
            while money > self._balance:
                self._condition.wait()
            new_balance = self._balance - money
            time.sleep(0.001)
            self._balance = new_balance

    @property
    def balance(self):
        return self._balance


def add_money(account):
    while True:
        money = randint(5, 10)
        account.deposit(money)
        print(threading.currentThread().name, ":", money, '====>', account.balance)
        time.sleep(0.5)

def sub_money(account):
    while True:
        money = randint(10, 30)
        account.withdraw(money)
        print(threading.currentThread().name, ':', money, '<====', account.balance)
        time.sleep(1)

def main():
    """主函数"""
    account = Account()
    #创建线程池
    with ThreadPoolExecutor(max_workers=15) as pool:
        for _ in range(5):
            pool.submit(add_money, account)
        for _ in range(5):
            pool.submit(sub_money, account)


if __name__ == '__main__':
    main()
