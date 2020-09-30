def main():
    num,rev=0,0
    n=input("enter n")
    num=n
    while (num > 0):
        rev=rev*10+num%10
        num=num/10
    if(n==rev):
        print"palindome"
    else:
        print"not palindrome"
main()
