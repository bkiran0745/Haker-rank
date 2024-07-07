def swap_case(s):
    s1 = list()
    uper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in s:
        if(i not in uper):
            s1.append(i.upper())
        else:
            s1.append(i.lower())
    ss = ''
    for i in s1:
        ss+=i
    return ss

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)