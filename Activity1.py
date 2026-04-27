#create class
class IOstring:

    #construnctor to set default value
    def __init__(self):
        self.str1=""

    def get_string(self):
        self.str1=input("Enter string: ")
    
    def printstring(self):
        print("Result is: ", self.str1.upper())

string1=IOstring()
string1.get_string()
string1.printstring()

    