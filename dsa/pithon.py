import sys
input = sys.stdin.readline
def main():
    t=int(input())
    candy=[]
    for i in range(2,5000):
        if len(set(str(i)))<=2:
            candy.append(i)
    while t>0:
        n=int(input())
        for c in candy:
            if len(set(str(c*n)))<=2:
                print(c)
                break
        t-=1
if __name__=='__main__':
    main()
