#printing the statement on the screen
print("Enter your marks out of 100:")
​
#taking the input
sub1 = int(input())
sub2 = int(input())
sub3 = int(input())
sub4 = int(input())
sub5 = int(input())
​
#calculating and priting the total as well as average
tot = sub1 + sub2 + sub3 + sub4 + sub5
print("Total is:", tot)
avg = tot/5
print("Average is:", avg)
​
#calculating the grades of the student
if avg>=90 and avg<=100:
    print("Your grade is A")
elif avg>=80 and avg<89:
    print("Your grade is B")
elif avg>=70 and avg<79:
    print("Your grade is C")
elif avg>=60 and avg<69:
    print("Your grade is D")
elif avg>=50 and avg<59:
    print("Your grade is E")
else:
    print("Your grade is F")
