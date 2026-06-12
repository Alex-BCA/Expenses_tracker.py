expenses=[]
amounts=[]
while True:
    print("****Expense Traker****")
    print("1.Add expense")
    print("2.View expense")
    print("3.View total expense")
    print("4.Delete expense")
    print("5.Exit")

    choice=input("Entedr your choice")
    if choice=="1":
        print("Add expense")
        a=input("Expense name:")
        b=int(input("Amount:"))
        expenses.append(a)
        amounts.append(b)
    elif choice=="2":
        print("View expense")
        for i in range(len(expenses)):
            print(expenses[i],"=",amounts[i])
    elif choice=="3":
        print("Total expenses")
        total=sum(amounts)
        print("Total amount =",total)
    elif choice=="4":
        print("Delete expense")
        name=input("Enter expense name:")
        if name in expenses:
            index=expenses.index(name)
            expenses.pop(index)
            amount.pop(index)
            print("Expense deleted")
        else:
            print("Do not found!")
    elif choice=="5":
        print("Thank you!!")
        break
    else:
        print("In-valid syntax")
