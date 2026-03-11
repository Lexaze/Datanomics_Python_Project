# -------- COLORS --------
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

# -------- DATA STORAGE --------


# tasks = [{"name":"Python Project", "priority":"High", "done":False}]
tasks = []


# -------- ADD TASK --------
def add_task():

    name = input("Enter task name: ")

    print("\nSelect Priority")
    print("1. High")
    print("2. Medium")
    print("3. Low")

    priority_map = {
        "1": "High",
        "2": "Medium",
        "3": "Low"
    }

    choice = input("Choose priority (1-3): ")

    if choice not in priority_map:
        print(RED + "Invalid priority." + RESET)
        return

    priority = priority_map[choice]

    tasks.append({
        "name": name,
        "priority": priority,
        "done": False
    })

    print(GREEN + "Task added successfully!" + RESET)


# -------- VIEW TASKS --------
def view_tasks():

    if not tasks:
        print(YELLOW + "No tasks available." + RESET)
        return

    print(CYAN + "\n--------- TASK LIST ---------" + RESET)

    for i, t in enumerate(tasks, start=1):

        status = "[✓]" if t["done"] else "[ ]"

        # Color based on priority
        if t["priority"] == "High":
            priority_color = RED
        elif t["priority"] == "Medium":
            priority_color = YELLOW
        else:
            priority_color = GREEN

        print(
            f"{i}. {status} {t['name']:<25} "
            f"{priority_color}{t['priority']}{RESET}"
        )


# -------- COMPLETE TASK --------
def complete_task():

    try:
        idx = int(input("Enter task number to complete: ")) - 1

        if not tasks[idx]["done"]:
            tasks[idx]["done"] = True
            print(GREEN + "Task marked as completed." + RESET)
        else:
            print(YELLOW + "Task already completed." + RESET)

    except (ValueError, IndexError):
        print(RED + "Invalid task number." + RESET)


# -------- DELETE TASK --------
def delete_task():

    try:
        idx = int(input("Enter task number to delete: ")) - 1

        removed = tasks.pop(idx)

        print(RED + f"Deleted task: {removed['name']}" + RESET)

    except (ValueError, IndexError):
        print(RED + "Invalid task number." + RESET)


# -------- MAIN LOOP --------
while True:

    print("\n" + CYAN + "Choose Action" + RESET)
    action = input(
        "(Add / View / Complete / Delete / Exit): "
    ).lower()

    if action == "add":
        add_task()

    elif action == "view":
        view_tasks()

    elif action == "complete":
        complete_task()

    elif action == "delete":
        delete_task()

    elif action == "exit":
        print(GREEN + "Closing application..." + RESET)
        break

    else:
        print(RED + "Invalid command." + RESET)


# -------- FINAL SUMMARY --------
done_count = sum(1 for t in tasks if t["done"])
pending_count = len(tasks) - done_count

print("\n" + CYAN + "="*25)
print("FINAL SUMMARY")
print(GREEN + f"Completed: {done_count}" + RESET)
print(YELLOW + f"Pending:   {pending_count}" + RESET)
print(CYAN + "="*25)
