# makemework
Fix the issues in this repo and make this program work. 

# Setup
1. Fork this repository
2. Clone your forked repository
3. Create a virtualenv and activate it
4. `pip install -r requirements.txt`
5. Run the test using the command `pytest -k e2e`

# Your assignment
Complete the weather shopper exercise using the code provided to you. Your assignment is to:

a. fix the errors in the existing code 
b. complete the payment structure using a code structure similar to what has been used for the other actions
c. use the same design patterns and programming style used in this repository

# How to proceed?
1. Run the test using the command `pytest -k e2e`
2. Observe, debug and fix the error
3. Test your fix
4. Commit your change and push
5. Repeat steps 1-4 for the next error

# Example working test
If you fix all the bugs in this code, your test should perform like the gif below:

![](working-weather-shopper-test.gif)

Remember, you should not stop at just fixing the existing code. You should also complete the instructions on the cart page.

# Debugging tips
Here are some useful debugging tips that do not involve the use of debugger:

1. Search for strings in all files 
2. Search for sub-strings in all files if the exact string does not exist
3. F12 to follow the definition of a method
4. Add debug messages to figure out the flow 
5. if True: trick (to get exact error messages, in the test, replace `try:` with `if True:` and comment out the `except` portion)
6. Read the log messages backwards 
7. Sometimes the error happens in the line before the failure!


# Notes:
1. Use Python3
2. We recommend using Visual Studio code as your IDE
3. We recomment using a virtualenv
4. You need to have Chrome driver installed
