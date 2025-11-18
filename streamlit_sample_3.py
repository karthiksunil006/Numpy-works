import streamlit

expense_title=[]

amounts=[]


exp=streamlit.text_input("Enter your expense title : ")
amount=streamlit.number_input("Enter the amount : ")

if streamlit.button("Add Expense"):

    expense_title.append(exp)
    amounts.append(amount)
    

if streamlit.button("Show Total"):
    result=0
    
    for i in amounts:
        result+=int(i)
    print(result)

    streamlit.success(f"your total : {result}")