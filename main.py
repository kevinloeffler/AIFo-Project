import os
import sys
import library.debug as DEBUG
import library.queryHelpers as Res
from library.Intents import Intents as IntentsClass
from library.User import User as UserClass
from library.Ressources import Ressources as Ressources
from google.cloud import dialogflow

### Debug Mode
if '-d' in str(sys.argv):
    DEBUG.init(True)
    print('DEBUG: Running in Debug Mode')
else:
    DEBUG.init(False)

### Project
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'private_key.json'
DIALOGFLOW_PROJECT_ID = 'chatbot-aiftestat-qvco'
LOCATION_ID = 'europe-west1'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'

### Session
sessionClient = dialogflow.SessionsClient()
session = sessionClient.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
sessionIsActive = True

### Handle Response
def handleResponse(response):
    intentId: str = Res.getIntent(response)
    Intents.handleIntents(intentId, response)


User = UserClass()
Intents = IntentsClass()
print(Ressources['welcomeMessage']())

while sessionIsActive:
    userInput = User.getInput('')

    if userInput in User.commands['quit']:
        sessionIsActive = False
        break
    elif userInput in User.commands['help']:
        print(Ressources['help']())
    elif userInput == '':
        continue
    else:
        textInput = dialogflow.TextInput(text=userInput, language_code=DIALOGFLOW_LANGUAGE_CODE)
        queryInput = dialogflow.QueryInput(text=textInput)
        try:
            response = sessionClient.detect_intent(
                request={"session": session, "query_input": queryInput})
        except Exception as e:
            print(e)
        handleResponse(response)


'''
print("Query text:", response.query_result.query_text)
print("Detected intent:", response.query_result.intent.display_name)
print("Detected intent confidence:", response.query_result.intent_detection_confidence)
print("Fulfillment text:", response.query_result.fulfillment_text)
'''
