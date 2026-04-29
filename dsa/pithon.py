import sys
input = sys.stdin.readline

def main():
    t=int(input())
    while t>0:
        cnt=0
        n=int(input())
        nums=list(map(int,input().split()))
        for i in range(n-1):
            if nums[i]==0:
                break
            else:
                nums[nums[i]-1]=0
                cnt+=1
        print(cnt)
        t-=1
        
if __name__=='__main__':
    main()
        
