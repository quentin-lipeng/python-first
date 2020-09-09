def main():
    print('this is main function')
    pass


# 如果导入此文件为被导入模块 则__name__为模块名称
# 当为主程序时 __name__为 __main__
if __name__ == '__main__':
    main()
    pass

if __name__ != '__main__':
    print('not main')
