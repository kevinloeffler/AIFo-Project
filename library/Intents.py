class Intents():
    '''This class maps and handles all different intent types.'''

    def __init__(self):
        super(Intents, self).__init__()


    ###### Intent Handlers

    def defaultWeclomeIntent():
        print('Default Welcome Intent')

    def rankingIntent():
        print('Ranking Intent')


    ###### Intent Map

    intentMap = {
        '5470f7a9-e155-4dcb-9cf3-ae8f0a213738': defaultWeclomeIntent,
        'ca567445-526c-488a-a44f-b17c2c226f3d': rankingIntent,
    }

    def handleIntents(self, intentId: str):
        self.intentMap[intentId]()
