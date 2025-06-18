# 多线程编程
import threading
from time import sleep
from random import randint


# 注：因为Python的全局解释器锁（GIL）限制了同一时间只能有一个线程执行Python字节码；这意味着，如果你想要并行执行多个任务，通常的做法是使用多进程而非多线程
#    Python的多线程为并发执行
def song():
    while True:
        print("准备唱歌")
        sleep(randint(1, 3))
        print("正在唱歌。。。")
        sleep(randint(1, 3))
        print("唱歌完成")
        sleep(randint(1, 3))


def song1(start: str, msg: str, end: str):
    while True:
        print(start)
        sleep(randint(1, 3))
        print(msg)
        sleep(randint(1, 3))
        print(end)
        sleep(randint(1, 3))


def dance():
    while True:
        print("准备跳舞")
        sleep(randint(1, 3))
        print("正在跳舞。。。")
        sleep(randint(1, 3))
        print("跳舞完成")
        sleep(randint(1, 3))


def dance1(start: str, msg: str, end: str):
    while True:
        print(start)
        sleep(randint(1, 3))
        print(msg)
        sleep(randint(1, 3))
        print(end)
        sleep(randint(1, 3))


if __name__ == '__main__':
    # 创建一个唱歌的线程
    song = threading.Thread(target=song)
    # args:默认为一个元组
    song1 = threading.Thread(target=song1, args=("准备唱歌1", "正在唱歌1。。。", "唱歌完成1"))
    # 创建一个跳舞的线程
    dance = threading.Thread(target=dance)
    # kwargs:默认为一个字典
    dance1 = threading.Thread(target=dance1, kwargs={"start": "准备跳舞1", "msg": "正在跳舞1。。。", "end": "跳舞完成1"})

    song.start()
    song1.start()
    dance.start()
    dance1.start()

    song.join()
    song1.join()
    dance.join()
    dance1.join()
