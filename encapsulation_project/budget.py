class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    def get_category_name(self):
        return self.__category_name
    
    def set_category_name(self, new_name):
        self.__category_name = new_name

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, new_budget):  
        if new_budget > 0:
            self.__allocated_budget = new_budget
            self.__remaining_budget = new_budget
        else:
            print("Invalid budget amount. Please enter a positive number.")

    def add_expense(self, expense_amount):
        if expense_amount > 0:
            if expense_amount <= self.__remaining_budget:
                self.__remaining_budget -= expense_amount
            else:
                print("Insufficient budget for this expense.")
        else:
            print("Invalid expense amount: Please enter a positive number.")

    def display_details(self):  
        print(f"Category Name: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget:.2f}")
        print(f"Remaining Budget: ${self.__remaining_budget:.2f}")
