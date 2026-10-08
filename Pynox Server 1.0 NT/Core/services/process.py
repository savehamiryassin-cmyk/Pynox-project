import subprocess
def process():
    print("Pynox Process Services")
    print("----------------------")
    task = subprocess.run(
        ["tasklist"],
        capture_output = True,
        text = True)
    print(task.stdout)
