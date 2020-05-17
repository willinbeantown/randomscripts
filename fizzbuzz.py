#!/usr/bin/env python3
# coding: utf-8
def fizzbuzz(num):
    f = 'fizz'
    b = 'buzz'
    if num%3==0 and num%5==0:
        print(f+b)
    elif num%3==0:
        print(f)
    elif num%5==0:
        print(b)
    else:
        print(num)
        return


def main():
    for n in range(100):
        n = n+1
        fizzbuzz(n)
    return


if __name__ == '__main__':
    main()
