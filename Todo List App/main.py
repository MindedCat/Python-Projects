user_prompt = "Enter todo:"

todo_list = []

while True:
    user_input = input(user_prompt)
    user_input = user_input.capitalize()
    todo_list.append(user_input)
    print(todo_list)

    #print("You entered:", user_input)
    #print("Next...")


#todos = [user_input1, user_input2, user_input3]
#print("Your todo list:", todos)