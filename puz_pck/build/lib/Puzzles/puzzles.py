def Alibabapuzzle(a,b,c,d):
    list = [a+b*c,a*b+c,a-b*c,a*b-c,a+b-c,a-b+c]
    print('YES' if d in list else 'NO')
def count_subarrays(length):
    print("please enter array elements")
    i=list(map(int,input().split()))
    res=len(i)
    m=[]
    for n in range(length):
        for j in range(n,length):
            m.append(i[j])
            if len(m) > 1:
                if m == sorted(m):
                    res+=1
        m=[]
    print(res)
def play_with_string(tries_num):
    print('Enter your word')
    s = input()
    for i in range(tries_num):
        order = input().split()
        if order[0] == "pop_back":
            s = s[0:-1]
        elif order[0] == "front":
            print(s[0])
        elif order[0] == "back":
            print(s[-1])
        elif order[0] == "sort":
            l = min(int(order[1]),int(order[2]))
            r = max(int(order[1]),int(order[2]))
            s = s[0:l-1] + ''.join(sorted(s[l-1:r])) + s[r:]
        elif order[0] == "reverse":
            l = min(int(order[1]),int(order[2]))
            r = max(int(order[1]),int(order[2]))
            s = s[0:l-1] + s[l-1:r][::-1] + s[r:]
        elif order[0] == "print":
            pos = int(order[1]) - 1
            print(s[pos])
        elif order[0] == "substr":
            l = min(int(order[1]),int(order[2]))
            r = max(int(order[1]),int(order[2]))
            print(s[l-1:r])
        elif order[0] == "push_back":
            s += order[1]