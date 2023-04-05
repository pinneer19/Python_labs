import re


class MyContainer:

    def __init__(self):
        self.__storage = dict()
        self.__user = None

    def add(self, items):
        if not items:
            print("Passed keys are empty")
        else:
            for item in items:
                self.__storage[self.__user].add(item)
            print("Success")

    def remove(self, item):
        if item in self.__storage[self.__user]:
            self.__storage[self.__user].remove(item)
            print("Item was removed from container")
        else:
            print(f"There isn't item {item} in container")

    def find(self, items):
        was_found = False
        for item in items:
            if item in self.__storage[self.__user]:
                print(item)
                was_found = True
        if not was_found:
            print("No such elements")

    def list(self):
        if not self.__storage[self.__user]:
            print("Container is empty!")
        else:
            print(*self.__storage[self.__user])

    def grep(self, regex):
        try:
            was_found = False
            for item in self.__storage[self.__user]:
                if re.match(regex, item):
                    print(item)
                    was_found = True
            if not was_found:
                print("No such elements")
        except re.error:
            print("Regex error!!")

    def save(self):
        file = f"{self.__user}.txt"
        with open(file, 'w') as file:
            file.write(' '.join(self.__storage[self.__user]))
        print(f"Container was saved to {self.__user}.txt")

    def load(self):

        try:
            with open(f"{self.__user}.txt", 'r') as file:
                container = set(file.read().split(' '))
                if not self.__storage[self.__user]:
                    self.__storage[self.__user] = container
                else:
                    self.add(container)  # error was *container
        except FileNotFoundError:
            print(f"File {self.__user}.txt doesn't exist!")

    def switch(self, user: str):
        if self.__user in self.__storage.keys():
            choice = input("Do you want to save your container(y - yes, n - no): ")
            while choice != 'y' and choice != 'n':
                choice = input("Try again..\nDo you want to save your container(y - yes, n - no): ")
            if choice == 'y':
                self.save()

        self.__user = user
        self.__storage[self.__user] = set()
        print(f"Switched to user {self.__user}")

        choice = input("Do you want to load container(y - yes, n - no): ")
        while choice != 'y' and choice != 'n':
            choice = input("Try again..\nDo you want to load container?")
        if choice == 'y':
            self.load()
