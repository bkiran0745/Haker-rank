import textwrap
def wrap(s,m):
    k = textwrap.TextWrapper(width=m)
    ss = k.wrap(text=s)
    kk = ss[-1]
    ss.pop()
    for i in ss:
        print(i)
    return kk
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)