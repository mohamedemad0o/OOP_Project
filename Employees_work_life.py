class Person:
    def __init__(self,name, money, mood , health_rate):
        self.name = name
        self.money = money
        self.mood = mood
        self.health_rate = health_rate

    def sleep(self,hours):
        if not isinstance(hours , int) or not 0< hours <24:
            raise ValueError(" hours must be a number between 0 and 24")

        if hours== 7 :
            self.mood = "happy"
        elif  hours < 7 :
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def eat(self , meals):
        if meals == 3 :
            self.health_rate = "100% hth"
        elif meals ==2 :
            self.health_rate = "75% hth"
        elif meals ==1 :
            self.health_rate = "50% hth"


    def buy(self , items):
        self.money = self.money - 10 *items

class Employee(Person) :
    def __init__(self,name ,money , mood , health_rate,emp_id, car, email, salary, distance_work=20):
        super().__init__(name,money ,mood,health_rate)
        self.emp_id = emp_id
        self.car = car
        self.email= email
        self.salary = salary
        self.distance_work = distance_work

    def work(self, hours):
        if not isinstance(hours, int) and 0<hours<24:
            raise ValueError("hours must be numbers and between (0,24)")

        if hours == 8 :
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self):
        self.car.run(self.distance_work,self.car.velocity)


    def refuel(self,gas_amount=100):
        self.car.refuel(gas_amount)

    def send_emails(self,to , subject ,body,receiver_name,sender_name):
        print(f"""
        from {self.email}
        To: {to}  
        subject: {subject}
        Dear {receiver_name}
        {body}
        BR
        {sender_name}
        """)

class Car:
    def __init__(self,car_name,fuel_rate,velocity):
        self.car_name = car_name
        self.fuel_rate = fuel_rate
        self.velocity = velocity

    def run(self,distance , velocity):
        self.velocity= min(max(velocity,0),200)
        needed_fuel = distance*(100/9)         #10KM distance = F-.1F --  10 KM  =.9 F -- 10KM = 9/10F --  F = 100/9KM
        if needed_fuel <= self.fuel_rate:
            self.fuel_rate-=needed_fuel
            self.stop(0)
        else:
            distance_covered = self.fuel_rate*9/100
            self.fuel_rate=0
            remaining_distance = distance-distance_covered
            self.stop(remaining_distance)

    def stop(self,remaining_distance):
        self.velocity = 0
        if remaining_distance == 0:
            print("You have arrived at your destination.")
        else:
            print(f"you still have {remaining_distance} KM to reach your destination")

class Office:
    employees_number_in_office = 0
    def __init__(self,office_name):
        self.office_name = office_name
        self.employees = []
        Office.employees_number_in_office+=1


    @classmethod
    def change_employees_number(cls,num):
        cls.employees_number_in_office=num

    def get_all_employees(self):
        return self.employees


    def get_employee(self,emp_id):
        for emp in self.employees:
            if emp.id == emp_id:
                return emp
        return None

    def hire(self,employee):
        self.employees.append(employee)
        Office.employees_number_in_office += 1

    def fire(self, emp_id):
        employee = self.get_employee(emp_id)
        if employee:
            self.employees.remove(employee)
            Office.employees_number_in_office -= 1

    def deduct(self,emp_id,deduction=-10):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary -= deduction

    def reward(self,emp_id,reward=10):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary += reward

    def check_lateness(self, emp_id, move_hour):
        emp = self.get_employee(emp_id)
        if emp:
            is_late = Office.calculate_lateness(9, move_hour, emp.distance_to_work, emp.car.velocity)
            if is_late:
                self.deduct(emp_id, 10)
            else:
                self.reward(emp_id, 10)

    @staticmethod
    def calculate_lateness(target_hour, move_hour,velocity,distance):
        time_of_arrival = (distance/velocity) + move_hour
        if time_of_arrival <= target_hour :
            return False
        else:
            return True
