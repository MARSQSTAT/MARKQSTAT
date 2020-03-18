import Trademark
# This is an abstract class and not directly instantiated, for a MARQSTAT object use Marq, for each country

    def __init__(self):
        # Constructor for this class.
        print('Trademark')
    def get_application_number(self):
        return self.application_number
    def get_ow

# This is a class that works trademark
class Source:

    def __init__(self):
        # Constructor for this class.
        print('Registered sources')

    def get_source(self):
        return 'Sources obtained'



# Swiss Instance of a trade mark
class ChTrademark(Trademark,Source):

    def get_source(self):
        print('hello')




class Marq(Trademark):
    pass