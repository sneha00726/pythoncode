def is_leap(year):
    leap=False

    if(year%4==0) and ((year%100!=0) or (year%400==0)):

        leap=True

    return leap

def main():
    #take input form user 
    year=int(input())
    y=is_leap(year)
    print(y)
if __name__=="__main__":
    main()