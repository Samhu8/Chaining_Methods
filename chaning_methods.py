# Create a file with the User class, including the __init__ with all the attributes,
# parameters and default values.

class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    # Add the display_info(self) method to the User class
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
            return self # added instead of False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print(f"Hello {self.first_name}, it is {self.is_rewards_member} that you are now a member. You have {self.gold_card_points} points!")
            return self # made the addition

    # have this method decrease the user's points by the amount specified
    def spend_points(self,amount):
        self.gold_card_points = self.gold_card_points - amount
        if self.gold_card_points < 0:
            print("Sorry, you don't have enough points. Cannot process request")
            return self
        else:
            print(f"Hello {self.first_name}, you now have {self.gold_card_points} points.")
            return self





user_1 = User("Don","Draper","madmen01@codingdojo.com", 45)
user_1.display_info().enroll().spend_points(50)

user_2 = User("Ted", "Lasso", "richmond01@codingdojo.com", 40)
user_2.enroll().spend_points(80).display_info()

user_3 = User("Michael","Scott", "dunder01@codingdojo.com", 42)
user_3.display_info().spend_points(40)

