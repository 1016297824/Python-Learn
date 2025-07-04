# 服务器端
import json
import multiprocessing
import socket
import threading
from typing import Union


class Server:
    """
    服务器类
    """
    # server_id: str = None  # 服务器ID
    # server_post: int = None  # 服务器端口
    # server_listen: int = None  # 监听数量
    socket_server: socket = None  # 服务器对象
    client_dict: dict[str, dict[str, Union[socket.socket, tuple[str, int]]]] = {}  # 客户端字典

    def __init__(self, server_id: str, server_post: int, server_listen: int):
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_server.bind((server_id, server_post))
        self.socket_server.listen(server_listen)

    def run(self):
        while True:
            conn, addr = self.socket_server.accept()
            print("客户端已连接：", addr)
            try:
                # 初次链接发送确认信息
                conn.send("connected_check".encode("utf-8"))
                # 接受客户端确认链接数据
                name: str = conn.recv(1024).decode("utf-8")
                if not name:
                    print("客户端未发送名称，断开连接")
                    break
                # 保存客户端信息
                self.client_dict[name] = {"socket_conn": conn, "socket_addr": addr}
                # 为每个客户端创建通信线程
                client_threading: threading = threading.Thread(target=self.handle_client, args=(conn, name))
                client_threading.start()
                # client_threading.join()
            except Exception as e:
                print(e)
                break
        conn.close()
        self.socket_server.close()
        print("服务器已关闭")

    # 处理客户端发送的数据
    def handle_client(self, conn: socket.socket, name: str):
        print("启动通信线程：" + name)
        while True:
            try:
                data: str = conn.recv(1024).decode("utf-8")
                data: dict = json.loads(data)
                if not data:
                    print("接收到的数据为空")
                    break
                # 处理接收到的数据
                form: str = data["from"]
                target: str = data["target"]
                msg: str = data["msg"]
                print("接收到来自%s的消息：%s" % (form, msg))

                client: dict[str, Union[socket.socket, tuple[str, int]]] = self.client_dict[target]
                client_conn: socket.socket = client["socket_conn"]
                print("client_conn:", client_conn)
                # client_id: str = client["socket_addr"][0]
                # client_post: int = client["socket_addr"][1]
                addr: tuple[str, int] = client["socket_addr"]
                # 向指定客户端发送数据
                print(f"向{target}客户端({addr})发送消息：{msg}")
                send_msg = {"from": name, "msg": msg}
                send_msg_json = json.dumps(send_msg)
                client_conn.send(send_msg_json.encode("utf-8"))
            except Exception as e:
                print(e)
                break
        conn.close()
        print("客户端链接已断开")


if __name__ == "__main__":
    server = Server("localhost", 8888, 5)
    # server_multiprocessing = multiprocessing.Process(target=server.run)
    # server_multiprocessing.start()
    # server_multiprocessing.join()
    server.run()
