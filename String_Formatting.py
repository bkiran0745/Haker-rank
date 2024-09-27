def print_formatted(number):
    # your code goes here
    w = len("{0:b}".format(number))
    for i in range(1, number+1):
        o = oct(i)
        h = hex(i).upper()
        b = bin(i)
        o = o.replace("0o","")
        h = h.replace("0X","")
        b = b.replace("0b","")
        print(str(i).rjust(w), o.rjust(w), h.rjust(w), b.rjust(w))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)