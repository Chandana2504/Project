#welcome to university score calculator
#enter your marks: Good luck
sub1=int(input())
sub2=int(input())
sub3=int(input())
sub4=int(input())
sub5=int(input())
sub6=int(input())
result=float(sub1+sub2+sub3+sub4+sub5+sub6)/6
if result>90:
    print("excellent",result)
elif result>=80 and result<90:
    print("Distintion",result)  