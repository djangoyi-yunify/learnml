import sys

def main():
    if len(sys.argv) > 1:  # 有参数传入
        print(f'Hello, {sys.argv[1]}!')
    else:  # 没有参数传入，打印默认信息
        print('Hello, World!')

if __name__ == "__main__":
    main()
