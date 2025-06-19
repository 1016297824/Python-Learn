# 递归
import os


# 演示os模块的三个基础方法
def os_show():
    # 获取当前目录下所有文件名称
    print(os.listdir("test"))
    # 判断目录是否存在
    print(os.path.isdir("test/a"))
    print(os.path.isdir("test/1.txt"))
    # 判断文件或目录是否存在
    print(os.path.exists("test/a"))
    print(os.path.exists("test/1.txt"))


def find_all_file(path: str, t=0):
    if not os.path.exists(path):
        print("路径不存在")
        return

    result_list = []
    t += 1
    path_list = os.listdir(path)
    for path_name in path_list:
        new_path = path + "/" + path_name
        if os.path.isdir(new_path):
            n = t - 1
            while n > 0:
                print("\t", end="")
                n -= 1
            print(path_name)
            result_list += find_all_file(new_path, t)
        else:
            n = t - 1
            while n > 0:
                print("\t", end="")
                n -= 1
            print(path_name)
            result_list.append(new_path)

    return result_list


if __name__ == '__main__':
    os_show()
    print()
    result_list = find_all_file("test")
    print(result_list)
