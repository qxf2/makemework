"""
This utility is for Custom Exceptions. 

a) Stop_Test_Exception
You can raise generic exceptions using just a string.
This is particularly useful when you want to end a test midway based on some condition
"""

class Stop_Test_Exception(Exception):
    "Raise when a critical step fails and test needs to stop"
    def __init__(self,message):
        "Initializer"
        self.message=message

    def __str__(self):
        "Return the message in exception format"
        return self.message



