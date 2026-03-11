# with open("tasks.txt", "w") as f:
#     string = '''JAJAJA'''
#     f.write(string)


# with open("tasks.txt", "a") as f:
#     string = '''JAJAJA'''
#     f.write(string)

with open ("tasks.txt" , "r") as f:
    for line in f.readlines():
        print(line)