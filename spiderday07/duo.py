import time
def sing():
    for x in range(1,6):
        print('我在唱最炫民族风')
        time.sleep(3)

def dance():
    for x in range(1,6):
        print('我在跳广场舞')
        time.sleep(2)
def main():
    sing()
    dance()


if __name__ == '__main__':
    main()