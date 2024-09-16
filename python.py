"""import calendar
a=int(input("enter ther yaer"))
b=int(input("enter the month"))
print(calendar.month(a,b))"""

"""from datetime import date
first_date =date (2003,9,25)
last_date =date (2024,2,22)
dealta = last_date - first_date
print(dealta.days)
"""
""""
class goe:
    name="jsnck"
    drink="dfd"
    def ramesh(self):
        print("enjoy")
    def suresh(self):
        print("sad")
ramesh=goe()
suresh=goe()
ramesh.name="ramesh"
suresh.name="suresh"
suresh.drink="yes"
ramesh.drink="no"
ramesh.ramesh()
print("drink",ramesh.drink)
print("drink",suresh.drink)
"""
"""
a=int(input("enter the number"))
if a%2==0:
    print("even number")
else:
    print("odd")
"""

"""class laptop:
    def __init__(self,ram,processor):
        self.ram=ram
        self.processor=processor
    def display(self,):
        print("ram:",self.ram)
        print("procssor",self.processor)
dell=laptop("8","i5")
dell.display()"""
"""
from datetime import date
first=date (2005,9,16)
last=date (2024,2,22)
c=last-first
print(c.days)

    """    
"""
class animal:
    def sound(self):
        print("animal make a sound")
class dog(animal):
    def sound(self):
        print("dog braks")
class bird(dog):
    def sound(self):
        print("bird sings")
obj=bird()
obj.sound()

"""
"""
class arun:
    def ar(*args):
        b=0
        for i in args:
            b+=i
            print(b)
v=arun()
v.ar(2,4,6)

"""
"""
a=int(input("enter first number"))
b=int(input("enter second number"))
c=a*b
class arun:
    def kumar(self):
        if c <=1000:
            print(a*b)
        else:
            print(a+b)
boj=arun()
boj.kumar()
      
"""
"""b=0


for i in range(1,11):
    sum=b+i
    print("current",i,"pre",b,"sum",sum)
    b=i

"""
"""
class laptop:
   
    def __init__(self):
        self.__p="arun"
    def arun(self):
        print(self.__p)"""
"""       
class lap(laptop):
    def __init__(self):
        laptop.__init__(self)
    
        print(self.__p)
"""

"""
a=7//4
print(a)

"""
"""
import random

def play_game():
    total_runs = 0
    overs = 0
    balls = 0
    wickets = 0

    while overs < 2:
        print("\nOver:", overs + 1)
        while balls < 6:
            player_input = input("Press Enter to bowl...")

            # Simulate the bowl
            runs = random.randint(0, 6)

            if runs == 0:
                print("Out! You got a wicket!")
                wickets += 1
                if wickets == 3:
                    print("All out!")
                    break
            else:
                print("You got", runs, "runs!")
                total_runs += runs

            balls += 1

        overs += 1
        balls = 0

    print("\nInnings Over!")
    print("Total Runs Scored:", total_runs)
    print("Wickets Fallen:", wickets)

def main():
    print("Welcome to Mini Cricket Game!")
    play_game()

if __name__ == "_main_":
        main()


"""
"""
from twilio.rest import Client

# Your Twilio account credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Function to send OTP via SMS
def send_otp(phone_number, otp):
    message = client.messages.create(
        to=phone_number,
        from_='your_twilio_phone_number',
        body=f'Your OTP is: {otp}'
    )
    print(f"OTP sent successfully to {phone_number}")

# Example usage
otp = '123456'  # Generate your OTP here
phone_number = '+919524436062'  # Receiver's phone number
send_otp(phone_number,otp)
        """

"""i=1
sum=0
while i<=100:
    sum=sum+i
    i=i+1
    print(sum)
"""
"""a=0
for i in range(1,4):
    a=a+i
    print(a)
"""
"""from datetime import date

class person:
    def __init__(self,name,country,age):
        self.name=name
        self.country=country
        self.age=age
    def calculator(self):
        self.age=date.today()
        print(self.age)
obj=person("arun","india",67)
obj.calculator()
print(obj.name)
print(obj.age)
"""
"""
class laptop:
    def hp (self):
        self.hp_price=100000
        brand="hp"
class laptop1(laptop):
    def k(self):
        print(self.hp_price)
obj=laptop1()
obj.k()

      """  

"""
class balaraman:
    def kumar(self):
        a=(input("about"))
        print(a)

class karthi(balaraman):
    def arun(self):
        a=(input("about"))
        print(a)
obj=karthi()"""

class a:
    def b(self):
        a="arun"
class c(a):
    def d(self):
        print(a)
obj=c()
obj.d














       


















              






        

