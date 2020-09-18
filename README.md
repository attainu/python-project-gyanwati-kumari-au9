# Food Delivery App(Swiggy)

This project is intended to implement and demonstrate features offered by Swiggy. It's written in python and offers all functionalities through instruction set given via command line.

## Requirements

Swiggy food delivery system implementation

### Modules Used

We have used two modules which is mentioned below:
import time(this is used for day,time & date formate)
import uuid(it is used to generate random/unique id)

### Approach Used

This project is based on OOP'S concept
Swiggy(class): In this class we have implemented different functionalities like on board Restaurant , manage restaurant  menu ,User  signup ,login & logout , search food, select food, get cart , place order , generate bill, payment, delivery status, customer feedback etc. 
Restaurant(class): In this class we have implemented different functionalities like manage restaurants details, status(open/close), get menu, add menu items , update menu, delete menu .
Foods (class): This class is created to capture food details currently there are only few required fields like name and price. But based on future requirements additional fields and functionalities can easily be added.
User(class): In this class we have implemented some  functionalities like manage user details, accept delivery status, reject delivery status.
Cart(class): In this class we have implemented some  functionalities like add food items, remove food items, modify quantity.
Orders(class): In this class we have implemented some  functionalities like  print bill, mange orders details.

#### Instruction to run

This program are driven based on instruction set. It accepts number of test cases as first input and then ready that many times to get instruction from command line. It performs operations based on given instruction and print result on screen.
Below are list of sample instruction sets.
14
CRR_REST| 1|Khana Khajana| ABC Square|7867767687|Ranchi
CRR_REST| 2|Hotel| ABC Square|7867767687|Ranchi
CRR_REST| 3|Dhaba| ABC Square|7867767687|Ranchi
ADD_MENU | 1 | Dal|25
ADD_MENU | 1 | Tea|20
ADD_MENU | 1 | Roti|20
ADD_MENU | 1 | Juice|50
ADD_MENU | 2 | Dal|25
ADD_MENU | 2 | Tea|20
ADD_MENU | 2 | Roti|20
ADD_MENU | 2 | Juice|50
ADD_MENU | 3 | Dal|25
ADD_MENU | 3 | Tea|20
ADD_MENU | 3 | Roti|20
ADD_MENU | 3 | Juice|50
SEARCH|Dal
SIGNUP|gyan|123|Gyan|Ranchi-jharkhand|8976543218|678943|Ranchi
LOGIN|gyan|123
SELECT|1|Dal|2
GETCART | 1
PLACEORDER | 1
LOGOUT
GETORDERDETAILS|1
DELETERESTAURANT|1
PAYMENT |5173970b|50
ORDERHISTORY|5173970b
DELIVERORDER|5173970b
FEEDBACK |5173970b|Good food !