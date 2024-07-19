a=int(input("Values of A: "));
b=int(input("Values of B: "));

print("Please select operation -\n" \
"1. Add\n" \
"2. Subtract\n" \
"3. Multiply\n" \
"4. Divide\n")

select = int(input("select option :" ));
if select ==1:
    print("addition is ", a+b)

elif select ==2:
    print("subtraction is ",b-a)

elif select ==3:
    print("multiply is ",a*b)
elif select ==4:
    print("division is ",b/a)