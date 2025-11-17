todos = []

while True:
    cmd = input('Command (add/list/quit): ').strip()
    if cmd == 'add':
        item = input('Todo: ')
        todos.append(item)
        print('Added!')
    elif cmd == 'list':
        print('Todos:')
        for i,t in enumerate(todos): print(i+1, t)
    elif cmd == 'quit': break
    else:
        print('Unknown command')