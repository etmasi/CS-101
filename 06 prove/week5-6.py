print("Answer to each of these questions by providing  a 1-10 rating score:")

loan_amount = int(input("How much is the amount  the loan? "))
credit_report = int(input("How solid is your credit report? "))
income_month = int(input("How high is your monthly income? "))
down_payment = int(input("How big is your down payment? "))

plan_loan = False

if loan_amount >= 6:
    if credit >= 7 and income >= 7:
        plan_loan = True
    elif credit >= 7 or income >= 7:
        if down_payment >= 8:
            plan_loan = True
        else:
            plan_loan = False

else:/* */
    if credit < 5:
        plan_loan = False
    else:
        if income >= 7 or down_payment >= 7:
            plan_loan = True
        elif income >= 5 and down_payment >= 5:
            plan_loan = True
        else:
            plan_loan = False

if plan_loan:
    print("Please, offer the client the  loan.")
else:
    print("The decision is negative. You should not loan the money.")