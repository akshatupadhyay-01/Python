tasks=[]

# To add any tasks 
def add():
  
    totalTasks=int(input("How may task you want to add today:"))

    for i in range(1,totalTasks+1):
       
      print("Enter task {i} :")
      tasksName=input()
      tasks.append(tasksName)
       
    print(f"Todays tasks are : {tasks}")


#To update any tasks
def update():
    totalUpdate=int(input("how many task you want to update :"))
    checkUpdate=input("Which task you want to update: ")
    
    if checkUpdate in tasks:
      for i in range(1,totalUpdate+1):
       index=tasks.index(checkUpdate)
       update=input(f"replace current task ({checkUpdate}) to :")
       tasks[index]=update
      print("Updated tasks :",tasks)
    else :
      print("task not found.")
      

#To clear all tasks
def clear():
  tasks.clear()

#To remove any tasks
def remove():
  rem=input("what you want to remove: ")
  tasks.remove(rem)
  print(f"After removing ({rem}) new tasks are:",tasks)


#Main game function calling block 
while True:
  print("------welcome in To Do List ------")  

  operation=int(input("Enter : 1(add) ,2(update),3(show tasks) ,4(clear) ,5(remove)"))
  if operation==1:
    add()
  elif operation==2:
     update()
  elif operation==3:
    print(f"Tasks : {tasks}")
  elif operation==4:
    clear()
  elif operation==5:
    remove()