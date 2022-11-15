
class Shark:
    def __init__(self, name):
        self.name = name

    def swim(self):
        print(self.name + " is swimming.")

    def be_awesome(self):
        print(self.name + " is being awesome.")
#constructor method for creating the Shark class.  it allows the shark to have a parameter for the name and defines the methods for swim and be_awesome.
def main():
    sammy = Shark("Sammy")
    sammy.be_awesome()
    stevie = Shark("Stevie")
    stevie.swim()
    Andrew = Shark("Andrew")
    Andrew.swim()
    Andrew.be_awesome()
# three sharks are created in the shark class and each calls upon one or both methods that can be called by the shark class.
if __name__ == "__main__":
  main()
  #sets the code as the main application instead of as a seperate function.