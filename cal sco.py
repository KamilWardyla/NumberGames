def calc_electric_scooter(cost_of_fuel, cost_of_scooter, cost_of_ticket):
    cost_all = cost_of_scooter
    count_month = 0
    count_cost_fuel = 0

    while count_cost_fuel < cost_all:
        cost_all += cost_of_ticket
        print(f"Koszty Hulajnoga + Bilety: {cost_all}")
        count_cost_fuel += cost_of_fuel
        print(f"Koszty paliwa : {count_cost_fuel}")
        count_month += 1
    return count_month


print(calc_electric_scooter(640, 2150, 150))