class MissingApiKey(Exception):
    """ custom class for no API key for API wrapper """
    def __init__(self):
        Exception.__init__(self, "No API Key for AlphaVantage was given")