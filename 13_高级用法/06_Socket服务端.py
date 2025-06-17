# Socket服务端入门
import socket

# 1.创建Socket对象
socket_sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket_sever = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)  # 此为IPv6和无连接模式的Socket对象

# 2.绑定IP地址和端口
socket_sever.bind(("localhost", 8888))

# 3.设置监听数量
socket_sever.listen(5)

# 4.等待客户端链接
'''
    conn:客户端和服务器端连接对象
    addr:客户端地址信息
'''
conn, addr = socket_sever.accept()  # 返回一个二元元组
# 注：accept()方法是阻塞方法，会等待客户端链接（没有客户端链接时，会一直阻塞）

print(f"客户端已连接,客户端信息：{addr}")

while True:
    # 5.接受客户端信息
    '''
        recv():缓冲区大小，一般为1024
        decode():将recv()返回的字节序列（bytes对象）解码为字符串对象
    '''
    data: str = conn.recv(1024).decode("UTF-8")
    print("客户端接收：", data)
    if data == "exit":
        print("客户端已退出")
        break

    # 6.回复客户端信息
    msg = input("请输入回复信息：")
    if msg == "exit":
        print("服务器已退出")
        conn.send("服务器已退出".encode("UTF-8"))
        break
    # print("服务器发送：", msg)
    conn.send(msg.encode("UTF-8"))

# 7.关闭链接
conn.close()
socket_sever.close()
