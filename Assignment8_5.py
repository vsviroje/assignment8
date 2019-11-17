from threading import *

def htl():
    for i in range(1, 50, 1):
        print(i)

def lth():
    for i in range(50, 0, -1):
        print(i)

def main():
    t1 = Thread(target=htl, args=())
    t2 = Thread(target=lth, args=())
    t1.start()
    t1.join()
    t2.start()
    t2.join()


if __name__ == '__main__':
    main()

