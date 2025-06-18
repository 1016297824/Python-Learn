# Socket客户端开发
import socket

# 1.创建Socket对象
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.链接服务器
socket_client.connect(("localhost", 8888))

while True:
    # 3.发送数据
    msg = input("请输入发送内容：")
    if msg == "exit":
        socket_client.send("客户端断开链接".encode("utf-8"))
        break
    socket_client.send(msg.encode("utf-8"))

    # 4.接收数据
    data:str = socket_client.recv(1024).decode("utf-8")
    print("接收到的数据为：", data)

# 5.关闭客户端
socket_client.close()