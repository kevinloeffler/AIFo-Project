'''
A library with helpfull ressources
'''

# Private methods
def __help():
    return """
    COMMAND:    ALT:    DESCRIPTION:
    help        h       Shows this help menu
    quit        q       Exits the app

    QUESTIONS YOU CAN ASK:
    What was the best movie in 2000?
    In what movies did Tom Cruise act?
    What movies did Christopher Nolan direct between 1990 and 2000?
    """

def __welcomeMessage():
    return "Welcome to 'Text to SQL'\nStart by typing a question, help, or quit"

# Exported dictionary
Ressources = {
    'help': __help,
    'welcomeMessage': __welcomeMessage,
}
