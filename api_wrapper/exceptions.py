class MissingApiKey(Exception):
    """ custom class for missing API key for API wrapper """
    def __init__(self):
        Exception.__init__(self, "No API Key for AlphaVantage was given")
