stack = []

def append():
    add = input('Input add paramenter:')
    stack.append(add)
def pop():
    if stack:
        print("from stack popped %s" % stack.pop())
def view():
    print(stack)


def Show_menu():
    while True:
        CMD = {'0':append,'1':pop,'2':view,'3':exit}
        prompt = """
        (0) push it
        (1) pop it
        (2) view it
        (3) exit
        Please input your choice(0/1/2/3): """
        choice = input(prompt).strip()[0]

        if choice not in '0123':
            print('Invalid paramenter')

        if choice == 3:
            break

        CMD[choice]()
if __name__ == '__main__':
    Show_menu()