Task 2: Interview Questions
1. How do you open and write to a file in Python?
You use the built-in open() function. To write to a file, you use the 'w' (write) mode. It's best practice to use a with statement, which handles closing the file automatically.
with open('filename.txt', 'w') as f:
    f.write('Hello, world!')

2. What are common file modes?
 * 'r' (Read): Default mode. Opens a file for reading, errors if the file doesn't exist.
 * 'w' (Write): Opens a file for writing. Creates the file if it doesn't exist, or truncates (empties) it if it does.
 * 'a' (Append): Opens a file for appending. Creates the file if it doesn't exist. New data is written to the end of the file.
 * 'r+': Opens a file for both reading and writing.
3. What's the use of .strip()?
.strip() is a string method that removes any leading (beginning) and trailing (end) whitespace, including spaces, tabs, and newline characters (\n). It's very useful for cleaning up data read from files.
4. How do lists work in Python?
A list is a built-in data structure that stores an ordered, changeable collection of items. Items can be of different data types and are enclosed in square brackets [].
my_list = [1, "hello", 3.14]
5. What is the difference between append() and insert()?
 * append(item): Adds a single item to the end of the list.
 * insert(index, item): Inserts an item at a specific position (index) in the list.
6. How can you remove elements from a list?
 * my_list.pop(index): Removes and returns the item at a specific index. If no index is given, it removes the last item.
 * my_list.remove(value): Removes the first item in the list that matches the specified value.
 * del my_list[index]: Deletes the item at a specific index using the del keyword.
7. What are context managers (with statement)?
A context manager is an object that defines the methods needed to use the with statement. The with statement simplifies resource management (like files or network connections) by automatically handling setup (__enter__) and teardown (__exit__) tasks. For files, it ensures the file is always closed, even if errors occur.
8. How do you loop through a file line by line?
You can iterate directly over the file object in a for loop. This is the most efficient way to read a file line by line.
with open('filename.txt', 'r') as f:
    for line in f:
        print(line.strip()) # .strip() removes the newline

9. What is a data structure?
A data structure is a specialized format for organizing, processing, retrieving, and storing data. It defines the relationship between the data and the operations that can be performed on it. Common Python data structures are lists, tuples, dictionaries, and sets.
10. What happens if the file doesn't exist?
 * If you open in Read ('r') mode, Python will raise a FileNotFoundError.
 * If you open in Write ('w') or Append ('a') mode, Python will create a new, empty file automatically.
 * 
