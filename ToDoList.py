todo_list=[]

# functions toadd a new task
def add_task():
    task=input("Enter a task:")
    todo_list.append({"Task": task,"Status":"pending"})
    print("New task added successfully 1\n")

# function to view all task
def view_task():
    print("Your ToDo List")
    if len(todo_list)==0:
        print("No pending tasks")
    else:
        for index,task in enumerate(todo_list,1):
            print(f"{index}.Task: {task['Task']} , Status:{task['Status']}")
    print("\n")

# function to remove the task
def remove_task():
    if len(todo_list)==0:
        print("\n List is empty")
    else:
        try:
            search_index=int(input("Enter the task number that you want to remove :"))-1
            if 0<=search_index<= len(todo_list):
                remove_task = todo_list.pop(search_index)
                print(f"Task Removed :{remove_task["Task"]}")
            else:
                print("Invalid task number")
        except ValueError:
            print("Please enter a valid task number")

# function for task_done
def task_done():
    if len(todo_list)==0:
        print("\n List is empty")
    else:
        try:
            search_index=int(input("Enter the task number that you want to mark as done :"))-1
            if 0<=search_index<= len(todo_list):
                todo_list[search_index]["Status"]="Done"
                print(f"Task {todo_list[search_index]['Task']} has been marked as done")
            else:
                print("Invalid task number")
        except ValueError:
            print("Please enter a valid task number")


    
# function to display menu
def menu():
    while(True):
        print("*** Main Menu ***")
        print("1.Add a new Task")
        print("2.View All tasks")
        print("3.Remove a task")
        print("4.Mark a task as completed")
        print("5.Exit ")

        choice=input("Enter your choice: ")
        if choice == "1":
            add_task()

        elif choice=="2":
            view_task()
        elif choice =="3":
            remove_task()

        elif choice=="4":
            task_done()
        elif choice =="5":
            print("Exiting the application")
            exit()
        else:
            print("Invallid choice!Try again")

menu()
