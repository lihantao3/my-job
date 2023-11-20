import threading


def action(*add):
    for arc in add:
        #打印当前线程
        print(threading.current_thread().getName() + " " + arc)

#传入参数
my_tuple = ("https://sany.com/python/",\
            "https://sany.com/java/",\
            "https://sany.com/bash/")

#创建线程
thread = threading.Thread(target=action, args=my_tuple)

#启动线程
thread.start()
thread.join()

for i in range(5):
    print(threading.current_thread().getName())


