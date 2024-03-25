try:
  
    with open('my_file.txt', 'w') as file:
        file.write("Hello, I am a junior developer. 1 in 1,000,000\n")
        file.write("202120222023\n")
        file.write("I am a web developer and a Machine learning engineer.\n")


    with open('my_file.txt', 'r') as file:
        print(file.read())

    with open('my_file.txt', 'a') as file:
        file.write("I have appended line 1.\n")
        file.write("I have appended line 2.\n")
        file.write("I can also append another line here!\n")

    with open('my_file.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("File not found error.")
except PermissionError:
    print("Permission error.")
finally:
    print("Program completed.")
