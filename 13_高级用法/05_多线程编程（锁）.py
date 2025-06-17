# 多线程编程锁的使用
import threading
from random import randint
from time import sleep

counts = 0
lock = threading.Lock()


def song():
    global counts
    while True:
        with lock:
            # counts += 1
            counts = counts + 1
            print(f"准备唱歌{counts}")
            sleep(randint(1, 3))
            print("正在唱歌。。。")
            sleep(randint(1, 3))
            print(f"唱歌完成{counts}")
            print()
            sleep(randint(1, 3))


# 问题：依然能访问并修改锁中的数据？？？
def dance():
    global counts
    while True:
        # with lock:
        # counts += 1
        counts = counts + 1
        print(f"准备跳舞{counts}")
        sleep(randint(1, 3))
        print("正在跳舞。。。")
        sleep(randint(1, 3))
        print(f"跳舞完成{counts}")
        print()
        sleep(randint(1, 3))


def rap():
    global counts
    while True:
        with lock:
            # counts += 1
            counts = counts + 1
            print(f"准备rap{counts}")
            sleep(randint(1, 3))
            print("正在rap。。。")
            sleep(randint(1, 3))
            print(f"rap完成{counts}")
            print()
            sleep(randint(1, 3))


if __name__ == '__main__':
    # 创建一个唱歌的线程
    song = threading.Thread(target=song)
    # 创建一个跳舞的线程
    dance = threading.Thread(target=dance)
    # 创建一个rap的线程
    rap = threading.Thread(target=rap)

    song.start()
    dance.start()
    rap.start()
