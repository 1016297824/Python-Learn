# 客户端
import socket


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
        self.socket_client.connect((server_id, server_post))
