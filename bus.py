#Reshma Rathakrishnan Mudaliar
#Assignment 10.1 Your Own Class
#Create own class based on a real object and make a demo program utilizing the class


#Creating class called BusMAchine
class BusMachine:
    #class variable called tax
    tax = 0.50
    #constructor method takes in number of tickets, and price range
    def __init__(self, number_ticket, price_range):
        #making data variables private
        self.__number_ticket = number_ticket
        self.__price_range = price_range
    
    #set method for tickets, takes in number of tickets as argument
    def set_number_ticket(self, number_ticket):
        #writing condition for ticket
        if self.__number_ticket < 0:
            print("Invalid number. Please try again")
            #raising valuewrror if wrong input is given
            raise ValueError
            
        else:
             self.__number_ticket = number_ticket
             return self.__number_ticket    
    
    #get method for tickets
    def get_number_ticket(self):
        #returning the number of ticket
        return self.__number_ticket
    
    #set method for price range, takes in price range as argument
    def set_price_range(self, price_range):
        #setting condition for price range
        if self.__price_range < 0:
            print("Invalid price range. Please try again")
            raise ValueError 
        else:
            self.__price_range = price_range 
            return         
    
    #get method for price range
    def get_price_range(self):
        #return the price range times the number of tickets from get number ticket method
        return float(self.__price_range) * int(self.get_number_ticket())
    
    #method to add tax to price range
    def add_tax(self):
        #add price range to the value returned by get price range method
        self.__price_range = float(self.get_price_range()) + self.tax
        return self.__price_range
    
    #method to ask if they would like a round trip ticket
    def round_trip(self):
        question = input("Would you like a return ticket? Please enter yes or no: ")
        #Setting condition based on user input
        if question == 'yes':
            return f"{2* self.add_tax()} for 2 trips"    
        elif question == 'no':
            return f"{self.add_tax()} for one trip"
    
    #method to ask if they would like a receipt
    def receipt(self):
        question = input("Would you like a receipt? Please enter yes or no: ")
        #setting condition based on user input
        if question == 'yes':
            return 'Please collect your ticket and receipt from the bottom of the machine.'
        elif question == 'no':
            return 'Please collect your ticket from the bottom of the machine.'                

#main function
def main():
    #variable called ticket collecting user input on no. of tickets
    ticket = input("Welcome to Fantasy Machine. Please enter the number of bus tickets you would like to have: ")
    #variable called price collecting user input on desired price range
    price = input("Please enter your desired price for each ticket: ")
    #calling the class BusMachine
    machine = BusMachine(ticket,price)
    #Final Statement prints the value returned fromt he round trip with the value entered for ticket, and ending with a receipt notice.
    print(f"You have been charged with ${machine.round_trip()} for {ticket} tickets including tax. {machine.receipt()}")
if __name__ == '__main__':
    main()                        