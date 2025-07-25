#Task 7:Read a File and Handle Errors 
try:
    with open('sample.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")







