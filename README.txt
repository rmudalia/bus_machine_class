CLASS DOCUMENTATION
Class Description
The class name is BusMachine, and its purpose is to utilize input given by users to return appropriate values for bus tickets and their price. The BusMachine class takes in number of tickets and price range as arguments. Values for both arguments are collected through user input. BusMachine contains 8 total methods-including the constructor method- which work together to return number of tickets, and their corresponding price.

Variable Description
The class variable is called tax with an assigned value of 0.50 units. It has been called in the add_tax method to add to the user's desired price range.
One of the data variable is number_ticket that has been used in the get_price_range() method and get_number_ticket() method. Value is assigned to this variable through user input.
The other data variable is price_range which has been used in the add_tax() method and the get_price_range() method. The value is assigned to this variable through user input.

Method Description
The constructor method takes in numer of tickets and price range as arguments. It also makes the data variables private, to be accessed by other methods.
The set_number_ticket() method takes in the number of tickets as an argument. It contains a if/else condition that decide whether the numebr of tickets are an appropriate value or an inapproriate value such as negative numbers. If the value is negative, it raises a ValueError.
The get_number_ticket() method does not take in any arguments. Its purpose is to return the correct number of tickets when called. This method was also called inside the get_price_range() method.
The set_price_range() method takes in price range as an argument. It contains an if/else condition that decide what value gets returned from the function. If the value is negative, then the fucntion raises a ValueError.
The get_price_range() method takes is no arguments. It returns the price times the number returned by the get_number_ticket() method.
The add_tax() method takes in no arguments. It returns the price from the get_price_range() function and adds the class variable 'tax' to it.
The round_trip() method takes in no arguments. It contains a variable 'question' that stores the response from the user on whether they would like to have return tickets as well. If they answer yes, the method returns the values from the add_tax() method times 2. If they say no, they will only be charged for 1 trip.
The receipt() method takes in no arguments. It contains a variable 'question' that asks the user if they would like a receipt. If the answer is yes, the method returns a statement telling the user to collect both their ticket and receipt. If the answer is no, the method returns a statement telling the user to collect just their ticket. 

DEMO PROGRAM
The program in the main function starts with asking the user on how many bus tickets they would like to buy from the Fantasy Machine. Then the user is asked to enter any amount they would like to pay for 1 ticket. After these 2 entries, the program will ask the user if they would like to pay for the return trip as well. While the transaction is being processed, the program finally asks the user if they would like a receipt. After all the entries have been taken into account, the program generates a statement telling the user that they have to pay a certain amount including tax for 1 or 2 trips. It will also ask the user to collect their ticket and the receipt if they asked for it.

DEMO PROGRAM NOTES
The program requires that the user enter only  a positive whole number for the ticket and only positive value for their desired price. When the program asks the user for a 'yes' or 'no' entry, it is important that the user enters only the lowercase forms of 'yes' or 'no'.