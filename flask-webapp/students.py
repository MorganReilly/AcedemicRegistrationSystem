"""
TITLE: students.py
ABOUT: Handler for Student endpoint
AUTHOR: Morgan Reilly
"""
# Data to serve with API
STUDENTS = {
    '1': {'name': 'Greg'},
    '2': {'name': 'Tina'}
}


# Create handler for GET request on Professors
def read():
    """
        This function responds to a request for /api/students
        with the complete lists of students

        :return:        sorted list of students
        """
    # Create the list of people from our data
    return [STUDENTS[key] for key in sorted(STUDENTS.keys())]
