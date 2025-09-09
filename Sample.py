# Grading System using elif in Python

marks = int(input("Enter your marks (0 - 100): "))

if marks >= 90:
    print("Grade: A+ (Excellent Performance)")
elif marks >= 75:
    print("Grade: A (Very Good Performance)")
elif marks >= 60:
    print("Grade: B (Good Performance)")
elif marks >= 45:
    print("Grade: C (Needs Improvement)")
else:
    print("Grade: Fail (Better luck next time)")

print("Marks Entered:", marks)
print("Grading Completed Successfully")

print("**********************************************************************************************************************************************")

# Nested If Example: ATM Withdrawal

balance = 5000
print("Welcome to ATM")
print("Your Current Balance:", balance)

amount = int(input("Enter withdrawal amount: "))

if amount <= balance:
    if amount % 100 == 0:
        print("Transaction Successful! Please collect your cash.")
        balance -= amount
        print("Remaining Balance:", balance)
    else:
        print("Enter amount in multiples of 100.")
else:
    print("Insufficient Balance.")

print("Thank you for using our ATM service")
