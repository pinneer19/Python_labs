ADD = "add"
REMOVE = "remove"
FIND = "find"
LIST = "list"
GREP = "grep"
SAVE = "save"
LOAD = "load"
SWITCH = "switch"
EXIT = "exit"
CLEAR = "clear"
HELP = "help"
HELP_ANSWER = """
Available container commands:
add <key>     - add one or more elements to the container (if the element is already in there then don’t add);
remove <key>  - delete key from container;
find <key>    - check if the element is presented in the container, print each found or “No such elements” if nothing is;
list          - print all elements of container;
grep <regex>  - check the value in the container by regular expression, print each found or “No such elements” if nothing is;
save          - save container to file;
load          - load container from file;
switch <user> - switches to another user.
exit          - exits from the program
"""