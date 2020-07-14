import os

result = []


def get_all(p):
    arr1 = os.listdir(p)  # 查看文件下的文件
    for i in arr1:
        s = os.path.join(p, i)  # 拼接文件和路径
        if os.path.isdir(s):  # 判断是否文件夹
            get_all(s)
        m = os.path.basename(i)  # 获取文件名
        result.append(m)
    return len(result)


if __name__ == '__main__':
    p1 = os.getcwd()
    print(get_all(p1))
