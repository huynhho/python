class FirstClass: # Define a class object
    def setdata(self, value): # Define class's methods
        self.data = value  # self is the instance
    def display(self):
        print(self.data) # self.data: per instance

print(x = FirstClass()) # Make two instances
y = FirstClass() # Each is a new namespace
