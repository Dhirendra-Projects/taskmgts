def task():
    tasks = [ ] #Empty list 
    print("----Welcoome in Task Management App----")
    total_task = int(input("Please enter how many task you want to add ="))
    for i in range(1,total_task+1):
         task_name =input(f"Enter task {i} =")
         tasks.append(task_name)

    print(f"Your today's tasks are \n {tasks} ") #You can show your tasks

    while True:
         operation =int(input(" Please Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n If Your want to Add,Update ,Delete ,View and Exit/Stop\n Please Enter No."))
         if operation == 1: # for the Addiing your new task
              add = input("Enter task you want to add=")
              tasks.append(add)
              print(f"Task {add} has been successfully added...")
         elif operation == 2: # for Update your task
              update = input("Enter the task name for update = ")
              if update in tasks:
                   up = input("Enter new task = ")
                   ind = tasks.index(update)  #0,1,2,3,4
                   tasks[ind]=up
                   print(f"Update task {up} ")
         elif operation == 3: # for Deleting your task
              delet = input("which task you want to delete = ")
              if delet in tasks:
                   ind = tasks.index(delet)
                   del tasks[ind]
                   print(f"Task {delet} has been deleted...")
         elif operation == 4: # for View your total tasks
              print(f" Your Total tasks = {tasks}") 
         elif operation == 5: # for Exit/Stop the Program
              print(f" Sorry!! Now Your pogram Stop ...")
              break
         else:
              print("Invalid input ")
task()         
            
              
          