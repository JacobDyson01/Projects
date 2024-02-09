import TaskManager as Task

if __name__ == '__main__':
    print("Welcome")
    taskList = {}
    while True:
        input1 = input("How can I help?: ")
        full_command = input1.split(":")

        command = full_command[0].strip().upper()
        if len(full_command) == 2:
            string = full_command[1].strip()
        else:
            string = ''

        if command == 'ADD':
            name = string
            text = input("Enter task description: ")
            task = Task.Task(name, text)
            taskList[name] = task
            print(f"Task '{name}' added successfully.")
        elif command == 'UPDATE':
            name = string
            if name not in taskList.keys():
                print(f"Task '{name}' not found.")
                continue
            text = input("Enter new task description: ")
            taskList[name].setText(text)
            print(f"Task '{name}' updated successfully.")
        elif command == "QUIT":
            break
        elif command == "DELETE":
            if string in taskList:
                del taskList[string]
                print(f"Task '{string}' deleted successfully.")
            else:
                print("Task not found.")
        elif command == "VIEW":
            for task_name, task_obj in taskList.items():
                print(f"Task: {task_name}, Description: {task_obj.getText()}\n")
        else:
            print("Invalid command.")
        """
        TODO: Add more functionality of the client: commands such as sort, complete, due dates, Add a GUI support?
        """
    print("GoodBye")
