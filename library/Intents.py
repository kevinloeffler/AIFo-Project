import library.querySqlImdb as qsi
# import json
# TODO use json to extract values

class Intents():
    '''This class maps and handles all different intent types.'''

    def __init__(self):
        super(Intents, self).__init__()


    ###### Intent Handlers

    def defaultWeclomeIntent(response):
        print('Default Welcome Intent')

    def rankingIntent(response):
        print('Ranking Intent')
        try:
            year = int(response.query_result.output_contexts[0].parameters['year'][0])
        except IndexError:
            year = []
        if(year == []):
            # test query, can be deleted
            query = """SELECT tb.primaryTitle, tr.averageRating from
                    title_ratings tr join title_basics tb on
                    tb.tconst = tr.tconst order by tr.numVotes desc,
                    tr.averageRating desc limit 5;"""
            qsi.query_sql_imdb(query)
        else:
            if(len(str(year)) == 4):
                query = f"""SELECT tb.primaryTitle, tr.averageRating from title_ratings tr
                        join title_basics tb on tb.tconst = tr.tconst where
                        tb.startYear = \'{year}\' order by tr.numVotes desc,
                        tr.averageRating desc limit 1;"""
                qsi.query_sql_imdb(query)
                # TODO message if emtpy query (e.g. year = 2049)
            else:
                # TODO
                print('Specify the year as YYYY')

    def defaultFallbackIntent(response):
        print('Default Fallback Intent')


    ###### Intent Map

    intentMap = {
        '5470f7a9-e155-4dcb-9cf3-ae8f0a213738': defaultWeclomeIntent,
        'ca567445-526c-488a-a44f-b17c2c226f3d': rankingIntent,
        '43828901-51a8-40bb-a234-31ddc371f216': defaultFallbackIntent,
    }

    def handleIntents(self, intentId: str, response: str):

        self.intentMap[intentId](response)
