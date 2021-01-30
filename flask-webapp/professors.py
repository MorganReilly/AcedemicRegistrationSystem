"""
TITLE: professors.py
ABOUT: Handler for Professor endpoint
AUTHOR: Morgan Reilly
"""
# Data to serve with API
PROFESSORS = {
    '1': {'name': 'Alice'},
    '2': {'name': 'Bob'}
}


# Create handler for GET request on Professors
def read():
    """
        This function responds to a request for /api/professors
        with the complete lists of professors

        :return:        sorted list of professors
        """
    # Create the list of people from our data
    return [PROFESSORS[key] for key in sorted(PROFESSORS.keys())]
