x= int(input())
if ((x%4==0) and not (x%100==0))or(x%400==0):
    print ('ДА')
else:
    print ('НЕТ')
