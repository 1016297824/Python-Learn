# 客户端
import json
import socket
import threading
from asyncio import sleep


class Client:
    """
        客户端类
    """
    # server_id: str = None  # 服务器ID
    # server_post: int = None  # 服务器端口
    socket_client: socket = None  # 客户端对象
    client_name: str = None  # 客户端名称
    client_target: str = None  # 目标客户端名称

    def __init__(self, server_id: str, server_post: int, client_name: str, client_target: str):
        self.client_name = client_name
        self.client_target = client_target
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.socket_client.setblocking(False)
        self.socket_client.connect((server_id, server_post))

    def run(self):
        # 第一次链接后通信
        try:
            first_data = self.socket_client.recv(1024).decode("utf-8")
            if first_data == "connected_check":
                name: str = self.client_name
                self.socket_client.send(name.encode("utf-8"))
        except  Exception as e:
            print(e)
            self.socket_client.close()
            print("服务器已关闭")
            return
        # 为接收数据开启一个线程
        get_data_threading = threading.Thread(target=self.get_data)
        # 为发送数据开启一个线程
        send_data_threading = threading.Thread(target=self.send_data)

        get_data_threading.start()
        send_data_threading.start()
        # get_data_threading.join()
        # send_data_threading.join()

    # 处理接收的数据
    def get_data(self):
        print("开始接收数据")
        while True:
            try:
                data = self.socket_client.recv(1024).decode("utf-8")
                # print(data)
                if not data:
                    print("接收到的数据为空")
                get_msg: dict = json.loads(data)
                print(f"接收到来自{get_msg['from']}的消息：{get_msg['msg']}")
            except Exception as e:
                print(e)
                self.socket_client.close()
                print("客户端已关闭")
                return

    # 循环发送数据
    def send_data(self):
        print("开始发送数据")
        while True:
            # sleep(200)
            try:
                # msg = input(f"请输入向{self.client_target}发送的内容：")
                msg = input()
                # msg="test"
                send_json = json.dumps({"from": self.client_name,
                                        "target": self.client_target,
                                        "msg": msg})
                self.socket_client.send(send_json.encode("utf-8"))
            except EOFError:
                print("输入流已关闭，无法继续发送消息。")
                self.socket_client.close()
                return
            except Exception as e:
                print(e)
                self.socket_client.close()
                print("客户端已关闭")
                return
