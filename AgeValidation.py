age=int(input("Enter your age :"))

if age >= 18 and age <= 100: 
    print ('You are eligible for vote')

elif age <= 18:
    print ('You are not eligible for vote')
    
else:
    print ('Enter valid Age')
    