# Python-Assignment-4-Submission

# Task 7: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
 
Program:

#Read a File and Handle Errors 
try:
    with open('sample.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")

Excepted Otput:
Error: The file 'sample.txt' does not exist.


Task 8: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
 
Program:

# Task 8: File Handling in Python

text_to_write = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text_to_write + "\n")
print("Data successfully written to output.txt.")

text_to_append = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(text_to_append + "\n")
print("Data successfully appended.")

print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:   
    content = file.read()
    print(content)
    
Expected Output:
Enter text to write to the file: Hello,Python!
Data successfully written to output.txt.
Enter additional text to append: Learning file handling in python
Data successfully appended.

Final content of output.txt:
Hello,Python!
Learning file handling in python

#thank you

