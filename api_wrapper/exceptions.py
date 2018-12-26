class MissingApiKey(Exception):
    """ custom class for missing API key for API wrapper """
    def __init__(self):
        Exception.__init__(self, "No API Key for AlphaVantage was given")

class ResponseError(Exception):
    """ custom class for error returned from AlphaVantage API """
    def __init__(self, *args):
        Exception.__init__(self, "{}".format(args[0]))
