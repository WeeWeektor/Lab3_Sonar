def read_file(filename):
    file = open(filename, 'r')
    data = file.read()
    return data


def dangerous_function(user_input):
    return eval(user_input)


def main():
    filename = "test.txt"

    if filename == "test.txt":
        print("Opening file:", filename)

    content = read_file(filename)
    print("File content:", content)

    result = dangerous_function("2 + 2")
    print("Eval result:", result)


main()
