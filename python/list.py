if __name__ == '__main__':
    N = int(input())
    my_list = []
    for _ in range(N):
        command, *arg = input().split()
        arg = tuple(map(int, arg))
        if command == 'insert':
            my_list.insert(arg[0], arg[1])
        elif command == 'print':
            print(my_list)
        elif command == 'remove':
            my_list.remove(arg[0])
        elif command == 'append':
            my_list.append(arg[0])
        elif command == 'sort':
            my_list.sort()
        elif command == 'pop':
            last_item = my_list.pop()
        elif command == 'reverse':
            my_list.reverse()
