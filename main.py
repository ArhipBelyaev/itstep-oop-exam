import random


class Bank:
    def __init__(self):
        self.available_funds = 10000

    def request_loan(self, amount):
        if amount <= self.available_funds:
            self.available_funds -= amount
            return amount
        else:
            return 0


class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Student:
    def __init__(self, nameuser):
        self.nameuser = nameuser
        self.happiness = 50
        self.progress = 0
        self.active = True
        self.money = 0
        self.years_lived = 0
        self.loan = 0
        self.car = None

    def to_study(self):
        print('Time to study!')
        self.progress += 0.30
        self.happiness -= 8

    def to_sleep(self):
        print('ZZZZZZ!')
        self.happiness += 1

    def to_chill(self):
        print('Chill time!')
        self.happiness += 1
        self.progress -= 0.2
        self.money -= 40

    def to_money(self):
        print('money-money-money-money')
        self.happiness += 1
        self.progress += 0.1
        self.money += 100

    def to_work_money(self):
        self.happiness += 1
        self.progress += 0.1
        self.money += 100

    def take_loan(self, amount):
        bank = Bank()
        loan_amount = bank.request_loan(amount)
        if loan_amount > 0:
            self.loan += loan_amount
            self.money += loan_amount
            print(f"You have taken a loan of {loan_amount}$")
        else:
            print("Sorry, the bank does not have sufficient funds to provide you a loan.")

    def repay_loan(self, amount):
        if amount <= self.money:
            self.money -= amount
            self.loan -= amount
            print(f"You have repaid {amount}$ of your loan.")
        else:
            print("You don't have enough money to repay the loan.")

    def buy_car(self, car):
        if self.money >= car.price:
            self.money -= car.price
            self.car = car
            print(f"You have bought a {car.name} for {car.price}$.")
        else:
            print("You don't have enough money to buy this car.")

    def is_active(self):
        if self.progress < -0.5:
            print('Vidrahuvaly((((')
            self.active = False
        elif self.happiness <= 0:
            print('Depression!')
            self.active = False
        elif self.progress > 10:
            print('Passes externally...')
            self.active = False
        elif self.money < -5:
            print('Go to work!!!')
            self.to_work_money()
        elif self.money < -6:
            amount = abs(self.money) * 10
            print(f'Add {amount} to money!')
            self.money += amount
        elif self.progress < 0:
            print('Problems with studying!')
            self.to_study()

    def status(self):
        print(f'Happiness: {self.happiness}')
        print(f'Progress: {round(self.progress, 2)}')
        print(f'Money: {round(self.money, 2)}$')
        print(f'Loan: {round(self.loan, 2)}$')
        if self.car:
            print(f'Car: {self.car.name}')
        else:
            print('Car: None')

    def live_a_day(self, day):
        day_str = f'Day {day} of {self.nameuser} life'
        print(f"{day_str:=^50}")
        d3 = random.randint(1, 4)
        if d3 < 1:
            self.to_study()
        elif d3 < 2:
            self.to_sleep()
        elif d3 == 3:
            self.to_chill()
        elif d3 == 4:
            self.to_money()
        self.status()
        self.is_active()

        if day % 365 == 0 and day > 0:
            self.years_lived += 1
            print(f'Congratulations, you have lived for {self.years_lived} year(s)!')
            self.active = False


nameuser = input("Write your name: ")
name = Student(nameuser=nameuser)

car1 = Car("Honda Civic", 5000)
car2 = Car("Toyota Camry", 8000)
car3 = Car("BMW X5", 15000)
car4 = Car("Mercedes-Benz E-Class", 20000)

cars = [car1, car2, car3, car4]

for day in range(1, 366):
    if name.active:
        name.live_a_day(day)
        if day % 30 == 0:
            choice = input("Do you want to take a loan or buy a car? (loan/car/n): ")
            if choice.lower() == "loan":
                loan_amount = int(input("Enter the loan amount: "))
                name.take_loan(loan_amount)
            elif choice.lower() == "car":
                print("Available cars:")
                for i, car in enumerate(cars):
                    print(f"{i+1}. {car.name} - {car.price}$")
                car_choice = int(input("Choose a car to buy (enter its number): "))
                if car_choice > 0 and car_choice <= len(cars):
                    name.buy_car(cars[car_choice-1])
                else:
                    print("Invalid car choice. Ignoring car options.")
            elif choice.lower() == "n":
                repayment_amount = int(input("Enter the loan repayment amount: "))
                name.repay_loan(repayment_amount)
            else:
                print("Invalid choice. Ignoring loan and car options.")
    else:
        break
