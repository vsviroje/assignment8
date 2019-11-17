from threading import *
import time
def evenfac(n):
    for i in range(1,n,1):
        if i%2==0 and n%i==0:
            print(i)
            n=n-1

def oddfac(n):
    for i in range(1,n,1):
        if i%2!=0 and  n%i==0:
            print("o",i)
            n=n-1


def main():
    n=10
    t1=Thread(target=evenfac,args=(n,))
    t2 =Thread(target=oddfac, args=(n,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__=='__main__':
    main()

