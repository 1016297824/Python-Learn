# 客户端：wyn
import multiprocessing

import client

if __name__ == '__main__':
    client_wyn = client.Client("localhost", 8888, "wyn", "zk")
    # multiprocessing_wyn = multiprocessing.Process(target=client_wyn.run)
    # multiprocessing_wyn.start()
    # multiprocessing_wyn.join()
    client_wyn.run()