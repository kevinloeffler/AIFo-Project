import re


def getYear(response) -> int:
    try:
        year = round(int(response.query_result.parameters['number']))
        return year
    except Exception as e:
        return -1

def getIntent(response) -> str:
    intentString = response.query_result.intent.name
    result = re.search(r'[a-z0-9]*/*/([a-zA-Z0-9\-]*)$', intentString)
    return result.group(1)
