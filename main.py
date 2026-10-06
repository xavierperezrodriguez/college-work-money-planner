#!/usr/bin/env python3
# College / Work / Money Planner
# This program compares work scenarios and estimates
# how each scenario affects a student's college funding gap.
print("COLLEGE / WORK / MONEY PLANNER")
print("--------------------------------")
print("Compare work scenarios and estimate your college funding gap.")
print()
college_cost = float(input("Enter total college cost: $"))
scholarships = float(input("Enter scholarships / financial aid: $"))
current_savings = float(input("Enter current savings: $"))
monthly_expenses = float(input("Enter monthly living expenses: $"))
months = int(input("Enter number of months to plan for: "))
# validate the main financial inputs
if (college_cost < 0 or scholarships < 0 or current_savings < 0
        or monthly_expenses < 0 or months <= 0):
    print()
    print("Financial values cannot be negative, and months must be greater than 0.")
    print("Please run the program again.")
else:
    # calculate costs that are the same for every scenario
    remaining_college_cost = college_cost - scholarships
    if remaining_college_cost < 0:
        remaining_college_cost = 0
    total_living_expenses = monthly_expenses * months
    print()
    number_of_scenarios = int(input(
        "How many work scenarios do you want to compare? "))
    if number_of_scenarios <= 0:
        print("You must enter at least 1 scenario.")
    else:
        # variables used to keep track of the best scenario
        best_scenario_name = ""
        best_final_balance = 0
        first_scenario = True
        print()
        print("ENTER WORK SCENARIOS")
        print("--------------------")
        for scenario_number in range(1, number_of_scenarios + 1):
            print()
            print("Scenario", scenario_number)
            scenario_name = input("Enter scenario name: ")
            hourly_wage = float(input("Enter hourly wage: $"))
            hours_per_week = float(input("Enter hours worked per week: "))
            weeks_worked = float(input("Enter number of weeks worked: "))
            # validate work information
            if hourly_wage < 0 or hours_per_week < 0 or weeks_worked < 0:
                print("Work values cannot be negative.")
                print("This scenario will not be compared.")
                continue
            # calculate the result for this scenario
            work_income = hourly_wage * hours_per_week * weeks_worked
            available_money = current_savings + work_income
            final_balance = (
                available_money
                - remaining_college_cost
                - total_living_expenses
            )
            print()
            print("RESULT FOR", scenario_name.upper())
            print("------------------------------")
            print(f"Remaining college cost: ${remaining_college_cost:,.2f}")
            print(f"Estimated work income:  ${work_income:,.2f}")
            print(f"Living expenses:        ${total_living_expenses:,.2f}")
            print(f"Available money:        ${available_money:,.2f}")
            if final_balance >= 0:
                print(f"Estimated surplus:      ${final_balance:,.2f}")
            else:
                funding_gap = abs(final_balance)
                print(f"Estimated funding gap:  ${funding_gap:,.2f}")
            # update the best scenario
            if first_scenario or final_balance > best_final_balance:
                best_scenario_name = scenario_name
                best_final_balance = final_balance
                first_scenario = False
        # display the best scenario
        if first_scenario == False:
            print()
            print("BEST SCENARIO")
            print("-------------")
            print(best_scenario_name)
            if best_final_balance >= 0:
                print(f"Projected surplus: ${best_final_balance:,.2f}")
            else:
                print(
                    f"Projected funding gap: ${abs(best_final_balance):,.2f}"
                )
print()
print("Planner complete.")
          
