# Haker-rank
def merge_the_tools(s, n):
    s1 = ''
    j = 0
    for i in s:
        j+=1
        if j == n:
            if i not in s1:
                s1 +=i
                print(s1)
                s1 = ''
                j=0
            else:
                print(s1)
                s1 = ''
                j=0
        else:
            if i not in s1:
                s1 += i
            else:
                continue
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)