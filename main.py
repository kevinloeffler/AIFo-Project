import os
import library.queryHelpers as Res
from library.Intents import Intents as IntentsClass
from library.User import User as UserClass
from library.Ressources import Ressources as Ressources
from google.cloud import dialogflow

### Project
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'private_key.json'
DIALOGFLOW_PROJECT_ID = 'chatbot-aiftestat-qvco'
LOCATION_ID = 'europe-west1'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'


text_to_be_analyzed = 'What was the most popular movie in the year 2000?'

### Session
sessionCliend = dialogflow.SessionsClient()
session = sessionCliend.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
sessionIsActive = True

### Handle Response
def handleResponse(response):
    Intents = IntentsClass()
    intentId: str = Res.getIntent(response)
    Intents.handleIntents(intentId)


User = UserClass()
print(Ressources['welcomeMessage']())

while sessionIsActive:
    userInput = User.getInput('')

    if userInput in User.commands['quit']:
        sessionIsActive = False
    elif userInput in User.commands['help']:
        print(Ressources['help']())
    elif userInput == '':
        continue
    else:
        textInput = dialogflow.TextInput(text=userInput, language_code=DIALOGFLOW_LANGUAGE_CODE)
        queryInput = dialogflow.QueryInput(text=textInput)
        try:
            response = sessionCliend.detect_intent(session=session, query_input=queryInput)
        except InvalidArgument:
            raise
        handleResponse(response)


'''
print("Query text:", response.query_result.query_text)
print("Detected intent:", response.query_result.intent.display_name)
print("Detected intent confidence:", response.query_result.intent_detection_confidence)
print("Fulfillment text:", response.query_result.fulfillment_text)
'''
