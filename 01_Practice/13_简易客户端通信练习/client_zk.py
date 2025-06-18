# 客户端：zk
import multiprocessing

from client import Client

if __name__ == '__main__':
    client_zk = Client("localhost", 8888, "zk", "wyn")
    # multiprocessing_zk = multiprocessing.Process(target=client_zk.run)
    # multiprocessing_zk.start()
    # multiprocessing_zk.join()
    client_zk.run()
