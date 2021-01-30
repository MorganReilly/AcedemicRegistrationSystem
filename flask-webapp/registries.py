"""
TITLE: registries.py
ABOUT: Handler for Registry endpoint
AUTHOR: Morgan Reilly
"""
# Data to serve with API
COURSE_REGISTRIES = {
    '1': {'c_id': '100', 's_id': '1'},
    '2': {'c_id': '100', 's_id': '2'},
    '3': {'c_id': '101', 's_id': '1'},
    '4': {'c_id': '101', 's_id': '2'}
}


# Create handler for GET request on Professors
def read():
    """
        This function responds to a request for /api/registries
        with the complete lists of registries

        :return:        sorted list of registries
        """
    # Create the list of people from our data
    return [COURSE_REGISTRIES[key] for key in sorted(COURSE_REGISTRIES.keys())]
