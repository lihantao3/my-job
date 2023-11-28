"""
下面的例子演示了100个线程向同一个银行账户转账（转入1元钱）的场景，
在这个例子中，银行账户就是一个临界资源，在没有保护的情况下我们很有可能会得到错误的结果。
"""
from time import sleep
from threading import Thread, Lock


#银行账户，模拟存钱功能
class Account():
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            self._lock.release()

    @property
    def balance(self):
        return self._balance


#线程类，模拟存钱多线程
class DepositThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self) -> None:
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    #创建100个存钱的线程向同一个账户存钱
    for _ in range(100):
        t = DepositThread(account, 1)
        threads.append(t)
        t.start()
    #等待所有线程执行完
    for t in threads:
        t.join()
    print('账户余额为：%.2f元' % account.balance)


if __name__ == '__main__':
    main()
