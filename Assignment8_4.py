from threading import *
def small(n):
    sum=0
    for i in range(len(n)):
        if n[i] >= 'a' and n[i] <= 'z':
            sum = sum + 1
    print("s", sum)
    print(current_thread().ident)

def big(n):
    sum=0
    for i in range(len(n)):
        if n[i]>='A'and n[i]<='Z':
            sum=sum+1
    print("b",sum)
    print(current_thread().ident)

def digital(n):
    sum=0
    for i in range(len(n)):
        if n[i] == '0'or n[i] == '1'or n[i] == '2' or n[i] == '3'or n[i] == '4'or n[i] == '5'or n[i] == '6'or n[i] == '7'or n[i] == '8'or n[i] == '9':
            sum = sum + 1
    print("b", sum)
    print(current_thread().ident)

def main():

    str="ABCert765"
    t1=Thread(target=small,args=(str,))

    t2 =Thread(target=big, args=(str,))

    t3=Thread(target=digital,args=(str,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
if __name__=='__main__':
    main()

