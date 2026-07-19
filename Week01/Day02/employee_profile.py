def calculate_salary_difference(current_salary, expected_salary):
    """
    Calculate the difference between the expected salary and the current salary.

    Parameters:
    current_salary (float): The current salary of the employee.
    expected_salary (float): The expected salary of the employee.

    Returns:
    float: The difference between the expected and current salary.
    """
    return expected_salary - current_salary

current_salary = 27
expected_salary = 40
salary_difference = calculate_salary_difference(current_salary, expected_salary)
print(f"My current salary is {current_salary}")
print(f"My expected salary is {expected_salary}")   
print(f"The difference is {salary_difference}")
percentage_difference = (salary_difference / current_salary) * 100
print(f"The percentage is {percentage_difference:.2f}%")