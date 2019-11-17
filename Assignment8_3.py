from threading import *
def even(n):
    sum=0
    for i in range(len(n)):
        if n[i]%2==0:
            sum=sum+n[i]
    print("e",sum)


def odd(n):
    sum=0
    for i in range(len(n)):
        if n[i]%2!=0:
            sum=sum+n[i]
    print("o",sum)

def main():
    l=[10,20,30,45,50,60,99,80,90]


    t1=Thread(target=even,args=(l,))

    t2 =Thread(target=odd, args=(l,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__=='__main__':
    main()

