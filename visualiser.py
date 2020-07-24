import time
import os


def display(values, current=None):
    output = "\033[03;0H"
    height = max(values)
    for i in range(height):
        for j, n in enumerate(values):
            if (height - i) <= n:
                char = "█"
                if j == current:
                    char = "\033[93m" + char + "\033[0m"
            else:
                char = " "
            output += f"  {char}"
        output += "\n"
    output += ("{:>3}" * len(values)).format(*values) + "\n"
    print(output)


def visualise(bubble, values, auto=False):
    terminal = os.get_terminal_size()
    cols_needed = len(values) * 3
    if cols_needed > terminal.columns:
        print("Terminal is not wide enough.")
        print(f"Currently {terminal.columns} columns but {cols_needed} needed.")
        return
    
    sorter = bubble(values)
    display(values)
    while True:
        if not type(auto) is bool:
            time.sleep(auto)
        else:
            input()
        try:
            current = next(sorter)
        except StopIteration:
            current = None
            break
        finally:
            if type(current) is int:
                current += 1
            display(values, current)

    print("\nFinished sorting.")