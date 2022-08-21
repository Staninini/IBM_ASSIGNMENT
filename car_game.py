def car():
    status = 'stopped'
    while True:
        text = input('>')
        if text == 'start' and status == 'stopped':
            print ('car is starting...')
            status = 'started'
        elif text == 'stop' and status == 'started':
            print ('car is stopping...')
            status = 'stopped'
        elif text == 'start' and status == 'started':
            print ('Car is already started')
        elif text == 'stop' and status == 'stopped':
            print ('Car is already stopped')
        elif text == 'quit':
            break
        else:
            print('Commmand not recognized')

if __name__ == '__main__':
    car()
    