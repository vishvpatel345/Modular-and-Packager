def save_text(text):

    file = open("data.txt", "a")
    file.write(text + "\n")
    file.close()


def read_text():

    try:
        file = open("data.txt", "r")
        print(file.read())
        file.close()

    except FileNotFoundError:
        print("File not found")