from restaurant import Restaurant
from cart import Cart
from order import Order
from user import User


class Swiggy:
    def __init__(self):
        self.restaurants = {}
        self.carts = {}
        self.orders = {}
        self.users = {}
        self.pay = {}
        self.odHistory = {}
        self.currentUser = None

    def addMenuItemToRestaurant(self, resId, name, price):
        if resId in self.restaurants:
            rest = self.restaurants[resId]
            rest.addMenuItems(name, price)
        else:
            print("ERROR : Invalid restaurant Id")

    def SearchFood(self, n):
        for key, rest in self.restaurants.items():
            print(key, rest)
            for i, val in rest.menu.items():
                print(i, val)
                if i == n:
                    print("Found", rest.name, val.name, val.price)
                    return
        print("NotFound")

    def signUp(self, userId, pwd, name, address, mobileNum, pinCode, city):
        if userId not in self.users:
            self.users[userId] = User(userId, pwd, name, address,
                                      mobileNum, pinCode, city)
            print("successfully signup!")
        else:
            print("User already exist")

    def logIn(self, userId, pwd):

        if userId not in self.users:
            print("Please signup")
        else:
            user = self.users[userId]
            if user.pwd == pwd:
                self.currentUser = user
                print("login successfully, Welcome {}!".format(user.name))
            else:
                print("password is not matching!")

    def logOut(self):
        print("Logout successful, Good Bye {}".format(self.currentUser.name))
        self.currentUser = None

    def selectFood(self, cartId, name, qty):
        cart = self.getCart(cartId)
        cart.addFoodItems(name, qty)
        return cart

    def getCart(self, cartid):
        if cartid in self.carts:
            return self.carts[cartid]
        else:
            cart = Cart(cartid)
            self.carts[cartid] = cart
            return cart

    def placeOrder(self, cartId):
        if self.currentUser is None:
            print("Please login to place order")
            return
        cart = self.carts[cartId]
        missing = None
        order = Order()
        order.userId = self.currentUser.userId
        for i, rest in self.restaurants.items():
            total = 0
            missing = False
            currPrice = [None]*len(cart.items)
            for i in range(len(cart.items)):
                food = cart.items[i]
                qty = cart.quantities[i]
                if food.name not in rest.menu:
                    missing = True
                    break
                food = rest.menu[food.name]
                currPrice[i] = food.price
                total += (int(qty) * float(rest.menu[food.name].price))
            if not missing:
                if order.totalAmount is None or order.totalAmount > total:
                    order.resId = rest.resId
                    order.totalAmount = total
                    order.prices = currPrice
        if not missing:
            order.payStatus = "pending"
            order.odrStatus = "created"
            order.fName = cart.items
            order.fQty = cart.quantities
            self.orders[order.odId] = order
            order.print()
            print("Order created successfull!")
        else:
            print("Order failed, all prodts not avlbl in a restaurant(s)")
        return order

    def getOrderDetails(self, odId):
        if odId in self.orders:
            temp = self.orders[odId]
            temp.printDetails()
        else:
            print("odId is not match")

    def addRestaurant(self, resId, name, address, mobileNum, city):
        res = Restaurant(resId, name, address, mobileNum, city)
        if resId not in self.restaurants:
            self.restaurants[resId] = res
        else:
            print("ERROR - Restaurant with same id already exists")

    def deleteRestaurant(self, resId):
        self.restaurants.pop(resId)

    def PaymentStatus(self, odId, x):
        if odId not in self.pay:
            self.pay[odId] = x
            print("payment successfully!")
        else:
            print("Failed!")

    def orderHistory(self, odId):
        if odId not in self.odHistory:
            self.odHistory = self.orders.copy()
            print("All order details:", self.odHistory)
        else:
            print("Already recorded exit!")

    def deliverOrder(self, odId):
        if odId in self.orders:
            order = self.orders[odId]
            order.payStatus = "Delivered"
            print("delivered succesfully!")
        else:
            print("Invalid Id!")

    def feedback(self, odrId, comment):
        order = self.orders[odrId]
        if order is None:
            print("Invalid order Id")
        else:
            order.comment = comment
            self.orders[odrId] = order


"""
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

"""
if __name__ == "__main__":
    s = Swiggy()
    tc = int(input())
    for i in range(tc):
        tokens = input().split("|")
        if (len(tokens[0]) <= 0):
            break
        if tokens[0] == "CRR_REST":
            s.addRestaurant(tokens[1].strip(), tokens[2].strip(),
                            tokens[3].strip(), tokens[4].strip(),
                            tokens[5].strip())
        elif tokens[0].strip() == "ADD_MENU":
            s.addMenuItemToRestaurant(tokens[1].strip(), tokens[2].strip(),
                                      tokens[3].strip())
        elif tokens[0].strip() == "SEARCH":
            s.SearchFood(tokens[1])
        elif tokens[0].strip() == "SIGNUP":
            s.signUp(tokens[1].strip(), tokens[2].strip(), tokens[3].strip(),
                     tokens[4].strip(), tokens[5].strip(), tokens[6].strip(),
                     tokens[7].strip())
        elif tokens[0].strip() == "LOGIN":
            s.logIn(tokens[1].strip(), tokens[2].strip())
        elif tokens[0].strip() == "SELECT":
            s.selectFood(tokens[1].strip(), tokens[2].strip(),
                         tokens[3].strip())
        elif tokens[0].strip() == "GETCART":
            s.getCart(tokens[1].strip())
        elif tokens[0].strip() == "PLACEORDER":
            s.placeOrder(tokens[1].strip())
        elif tokens[0].strip() == "LOGOUT":
            s.logOut()
        elif tokens[0].strip() == "GETORDERDETAILS":
            s.getOrderDetails(tokens[1].strip())
        elif tokens[0].strip() == "DELETERESTAURANT":
            s.deleteRestaurant(tokens[1].strip())
        elif tokens[0].strip() == "PAYMENT":
            s.PaymentStatus(tokens[1].strip(), tokens[2].strip())
        elif tokens[0].strip() == "ORDERHISTORY":
            s.orderHistory(tokens[1].strip())
        elif tokens[0].strip() == "DELIVERORDER":
            s.deliverOrder(tokens[1].strip())
        elif tokens[0].strip() == "FEEDBACK":
            s.feedback(tokens[1].strip(), tokens[2].strip())
        else:
            print("ERROR - Unsupported instruction")
