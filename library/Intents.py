import library.querySqlImdb as qsi
import library.debug as DEBUG
# import json
# TODO use json to extract values

class Intents():
    '''This class maps and handles all different intent types.'''

    def __init__(self):
        super(Intents, self).__init__()


    ###### Intent Handlers

    def defaultWeclomeIntent(response):
        DEBUG.log('Default Welcome Intent')
        print(response.query_result.fulfillment_text)

    def rankingIntent(response):
        DEBUG.log('Ranking Intent')

        try:
            year = int(response.query_result.output_contexts[0].parameters['year'][0])
        except IndexError:
            year = -1

        if(year == -1):
            DEBUG.log('Empty Year')
            print('What year?')
        else:
            query = f"""SELECT
            tb.primaryTitle,
            tr.averageRating
            FROM title_ratings tr
            JOIN title_basics tb
            ON tb.tconst = tr.tconst
            WHERE tb.startYear = \'{year}\'
            ORDER BY tr.numVotes DESC,
            tr.averageRating DESC
            LIMIT 1;"""

            result = qsi.query_sql_imdb(query)

            if result == -1:
                print('An error occured')
            elif result == 0:
                print(f'No movie found for the year {year}')
            else:
                print(f"The best movie in {year} was '{result[0][0]}' with an average ranking of '{result[0][1]}'")


    def defaultFallbackIntent(response):
        DEBUG.log('Default Fallback Intent')
        print(response.query_result.fulfillment_text)


    ###### Intent Map

    intentMap = {
        '5470f7a9-e155-4dcb-9cf3-ae8f0a213738': defaultWeclomeIntent,
        'ca567445-526c-488a-a44f-b17c2c226f3d': rankingIntent,
        '43828901-51a8-40bb-a234-31ddc371f216': defaultFallbackIntent,
    }

    def handleIntents(self, intentId: str, response: str):

        self.intentMap[intentId](response)
