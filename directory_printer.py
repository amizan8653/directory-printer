import sys
import os

indent_length = 2
input_directory = sys.argv[1]

print(sys.argv)

def print_directory_structure(directory, depth):
    if os.path.isdir(directory):
        files = [os.path.join(directory, file) for file in os.listdir(directory)]
        for i in range(len(files)):
            file = files[i]
            file_name = os.path.basename(file)
            if os.path.isdir(file):
                if depth == 0:
                    print("+-", file_name)
                else:
                    print("|", end="")
                    print(" " * indent_length * depth, end="")
                    if i != len(files) - 1:
                        print("+-", file_name)
                    else:
                        print("\-", file_name)
                print_directory_structure(file, depth + 1)
            else:
                print("|", end="")
                print(" " * indent_length * depth, end="")
                if i != len(files) - 1:
                    print("+-", file_name)
                else:
                    print("\-", file_name)

print(os.path.basename(input_directory))
print_directory_structure(input_directory, 0)
