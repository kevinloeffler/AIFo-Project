class User():
    '''This class represents a user and what they can do'''

    def __init__(self):
        super(User, self).__init__()

    commands = {
        'quit': ['Q', 'q', 'stop', 'quit', 'end'],
        'help': ['H' '-H', '--H', 'h', '-h', '--h', 'Help', '-Help', '--Help', 'help', '-help', '--help']
    }

    def getInput(self, question: str) -> str:
        if question == '':
            userInput = input('>>> ')
        else:
            userInput = input(question + '\n>>> ')
        return userInput
