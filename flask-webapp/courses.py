"""
TITLE: courses.py
ABOUT: Handler for Course endpoint
AUTHOR: Morgan Reilly
"""
# Data to serve with API
COURSES = {
    '101': {'name': 'Maths', 'p_id': '1'},  # Example of single professor
    '102': {'name': 'English', 'p_id': '2'},
    '103': {'name': 'Latin', 'p_id': [1, 2]}  # Example of multiple professors
}


# Create handler for GET request on Professors
def read():
    """
        This function responds to a request for /api/courses
        with the complete lists of courses

        :return:        sorted list of courses
        """
    # Create the list of people from our data
    return [COURSES[key] for key in sorted(COURSES.keys())]
