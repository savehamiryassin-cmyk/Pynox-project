import os

def program(User):
    run = User[26::]
    print("Pynox Program Service")
    print("---------------------")
    if run.endswith(".py") or run.endswith(".pyw"):
        os.system("python " + run)
        print(f"Pynox Program Service running {run}")
    elif not run.endswith(".py"):
        print("Pynox Program Service only run python file without .py or .pyw please try again")