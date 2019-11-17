from threading import *
import time
def even(n):
    for i in range(1,n,1):
        if i%2==0:
            print(i)
            n=n-1

def odd(n):
    for i in range(1,n,1):
        if i%2!=0:
            print("o",i)
            n=n-1


def main():
    
    t1=Thread(target=even,args=(10,))
    t2 =Thread(target=odd, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__=='__main__':
    main()

