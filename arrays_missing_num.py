"""def missing_num(a):
    n=a[-1]
    expected=n*(n+1)/2
    actual=sum(a)
    p=expected-actual
    return p
a=[1,2,3,4,5,7,8]
print(missing_num(a))"""

import array as arr
a=arr.array('i',[12,3,4])
a.sort()
print(a)