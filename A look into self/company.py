# This file has practically no purpose. It is just a quick look into the 'self' object from classes.

class Employee:
    def __init__(self, name : str, base_salary : int, productivity : float, tier : int, tax_rate : float):
        self.name = name
        self.base_salary = base_salary
        self.productivity = productivity
        self.tier = tier
        self.tax_rate = tax_rate

    # Salary:
    # Job tier 1 - 5
    # Base salary 15,000 - 25,000
    # Tax rate 0.05 to 0.4
    # Name penalty: if their name starts with 'B', 0.8, else, 1

    def salary_calculation(self):
        if self.name[0].upper() == 'B': penalty = 0.8
        else: penalty = 1

        monthly_salary = (self.base_salary * self.tier * (1 - self.tax_rate) * penalty) / 12
        return round(monthly_salary, 2)

    # Likelihood of getting fired:
    # Base salary / 100,000
    # Name starts with a B
    # Productivity 0 -> 1

    def fired_probability(self):
        if self.name[0].upper() == 'B': penalty = 0.2
        else: penalty = 0
        chance = 1 / self.productivity * self.base_salary / 100_000 + penalty
        return min(1, chance)

    def output(self):
        return f"{self.name} has monthly salary of ${self.salary_calculation()} and a {self.fired_probability()} chance of being discharged per anum."


if __name__ == "__main__":
    file = open("A look into self/data.info", "w")
    bobby = Employee("bobby", 24999, 0.89, 4, 0.3).output()
    robby = Employee("robby", 24999, 0.69, 3, 0.15).output()
    file.write(f"{bobby}\n{robby}\n")  
    file.close()