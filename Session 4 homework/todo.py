# build a command line interface (CLI) tool that actually remembers your life.
#  Features add task, view task, mark any task as complete save and load startup,

import json
import os
from datetime import datetime

FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE): return []
    with open(FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def main():
    tasks = load_tasks()
    while True:
        print("\n--- THE LIFE LOG ---")
        if not tasks:
            print(" (Empty - Use 'add' to start a memory)")
        
        for i, task in enumerate(tasks):
            status = "✔" if task['done'] else " "
            # Display time if it exists
            created = task.get("created_at", "N/A")
            print(f"{i + 1}. [{status}] {task['text']} (Created: {created})")
        
        print("\nCommands: add [task], done [index], del [index], quit")
        user_input = input("> ").strip().split(" ", 1)
        cmd = user_input[0].lower()

        if cmd == "quit":
            break

        elif cmd == "add" and len(user_input) > 1:
            new_task = {
                "text": user_input[1],
                "done": False,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            tasks.append(new_task)

        elif cmd == "done" and len(user_input) > 1 and user_input[1].isdigit():
            idx = int(user_input[1]) - 1
            if 0 <= idx < len(tasks):
                tasks[idx]["done"] = True
                # Add a completion timestamp
                tasks[idx]["text"] += f" (Finished: {datetime.now().strftime('%H:%M')})"
            else:
                print("Invalid index!")

        elif cmd == "del" and len(user_input) > 1 and user_input[1].isdigit():
            idx = int(user_input[1]) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
            else:
                print("Invalid index!")
        else:
            print("Invalid command! Try: 'add coffee', 'done 1', or 'del 1'")
            continue
            
        save_tasks(tasks)

if __name__ == "__main__":
    main()

