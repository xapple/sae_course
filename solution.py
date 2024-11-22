def get_sales_data(employee_id):
    # Sales data with employee names
    sales = {'alice': 500, 'bob': 0}
    return sales.get(employee_id, 0)

def calculate_bonus(employee_id):
    sales = get_sales_data(employee_id)
    return compute_bonus(sales)


def compute_bonus(sales):
    target = 100
    if sales == 0:
        raise ErrorEmployeeFlemmard("On a un proble,me Houston")
    bonus_ratio = 10 / (sales / target)
    return bonus_ratio * sales

bonus = calculate_bonus('alice')
bonus = calculate_bonus('bob')
print(bonus)

