import math
import sys
import random
import os
import re

def main():
    #take input form user
    n=int(input().strip())

    if n%2!=0:
        print('Weird')
    elif n%2==0 and 2<= n <=5:
        print('weird')

    elif n%2==0 and 6<= n <=25:
        print('werid')

    elif n%2==0 and n>20:
        print('Not weird ') 

if __name__=="__main__":
    main()