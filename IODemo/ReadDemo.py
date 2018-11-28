# 下面的案例是不规范的，finally关闭不了输出流
# try:
#     f = open("1IODemo.iml")
#     print(f.read())
# except FileNotFoundError as e:
#     print(e)
# finally:
#     f.close()
#这里会自动执行关闭流，但是我想打印日志
# with open("IODemo.iml", "r") as f:
#     print(f.read())
# try:
#     with open("IODemo.iml", "r",encoding='UTF-8',errors="ignored") as readFile:
#         # print(f.read())
#         # 每次读取i个字节
#         # print(f.read(1))
#         # 每次读取一行
#         # print(f.readline())
#         # 按行读取,返回list,返回格式会乱，不影响
#         # for line in f.readlines():
#         #     print(line.strip())
#         print(readFile.read(1024))
# except Exception as e:
#     print(e)
# try:
#     with open("IODemo.txt", "w",encoding='UTF-8',errors="ignored") as writeFile:
#         writeFile.write("hello word");
#         # print(f.read())
#         # 每次读取i个字节
#         # print(f.read(1))
#         # 每次读取一行
#         # print(f.readline())
#         # 按行读取,返回list,返回格式会乱，不影响
#         # for line in f.readlines():
#         #     print(line.strip())
# except Exception as e:
#     print(e)
def readFile(path):
    try:
        with open(path,"r") as f:
            print(f.__exit__())
    except FileNotFoundError as e:
        return False,e

print(readFile("测试文件"))





