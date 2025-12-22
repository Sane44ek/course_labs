import typer
import sys


def main():
    """
    Говорит "Hello appsec world" пользователю, запрашивая имя интерактивно.
    """
    v = sys.version_info[0]
    
    if v == 3:
        name = input("Enter your name: ").strip()
    elif v == 2:
        # Python 2 (хоть и устарел, но для совместимости)
        name = raw_input("Enter your name: ").strip()
    else:
        print("Unknown Python version")
        return
    
    print(f"Hello appsec world from {name}")


if __name__ == "__main__":
    typer.run(main)
