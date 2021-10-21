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
            year = int(response.query_result.parameters['year'][0])
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

    def directorIntent(response):
        DEBUG.log('Director Intent')

        directors = []
        limit = None

        try:
            directorsProto = response.query_result.parameters['director']
            for director in directorsProto:
                directors.append(director['name'].lower())
        except Exception as e:
            DEBUG.log(e)
            print('Error: No Director given')

        try:
            limit = response.query_result.parameters['numberOfMovies']

            if(limit):
                limit = int(limit['top_number'])
        except Exception as e:
            print(e)

        if limit and len(directors) == 1:
            query = f"""
            SELECT tb.primarytitle, tr.averagerating
            FROM title_basics AS tb
            INNER JOIN title_ratings tr ON (tb.tconst = tr.tconst)
            INNER JOIN (
              SELECT tp.tconst, tp.category
              FROM title_principals AS tp
              WHERE nconst = (
                SELECT nb.nconst
                FROM name_basics AS nb
                WHERE lower(nb.primaryname) = '{directors[0]}'
                AND (nb.primaryprofession LIKE '%director%'
                OR nb.primaryprofession LIKE '%producer%')
              )
            ) AS principals ON (tb.tconst = principals.tconst)
            WHERE tb.titletype = 'movie'
            ORDER BY tr.averagerating DESC
            LIMIT {limit};
            """
            result = qsi.query_sql_imdb(query)

            if(result == 0 or result == -1):
                print(f'No results for {directors[0].title()}')
            else:
                print(f'The top {limit} movies directed by {directors[0].title()} are:')
                for movie in result:
                    print(f'{movie[0]}, rated: {movie[1]}')

        elif limit:
            print(f'Do query with directors: {directors} and limit: {limit}')

        elif len(directors) == 1:
            query = f"""
            SELECT tb.primarytitle, tr.averagerating
            FROM title_basics AS tb
            INNER JOIN title_ratings tr ON (tb.tconst = tr.tconst)
            INNER JOIN (
              SELECT tp.tconst, tp.category
              FROM title_principals AS tp
              WHERE nconst = (
                SELECT nb.nconst
                FROM name_basics AS nb
                WHERE lower(nb.primaryname) = '{directors[0]}'
                AND (nb.primaryprofession LIKE '%director%'
                OR nb.primaryprofession LIKE '%producer%')
              )
            ) AS principals ON (tb.tconst = principals.tconst)
            WHERE tb.titletype = 'movie'
            ORDER BY tb.primarytitle;
            """
            result = qsi.query_sql_imdb(query)

            if(result == 0 or result == -1):
                print(f'No results for {directors[0].title()}')
            else:
                print(f'{directors[0].title()} directed the following movies:')
                for movie in result:
                    print(f'{movie[0]}, rated: {movie[1]}')

        else:
            print(f'Do query with directors: {directors}')

    def defaultFallbackIntent(response):
        DEBUG.log('Default Fallback Intent')
        print(response.query_result.fulfillment_text)


    ###### Intent Map

    intentMap = {
        '5470f7a9-e155-4dcb-9cf3-ae8f0a213738': defaultWeclomeIntent,
        'ca567445-526c-488a-a44f-b17c2c226f3d': rankingIntent,
        '43828901-51a8-40bb-a234-31ddc371f216': defaultFallbackIntent,
        '8ce7a2cc-290d-4f8c-b0ef-8c7a3b549975': directorIntent,
        '0d912c47-c4a0-4089-82ac-16e7f7136200': directorIntent,
    }

    def handleIntents(self, intentId: str, response: str):

        self.intentMap[intentId](response)
