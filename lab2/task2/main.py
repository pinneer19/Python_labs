from container import MyContainer
from utilities import get_command, run_container


def main():
    container = MyContainer()
    run_container(container)


if __name__ == "__main__":
    main()
