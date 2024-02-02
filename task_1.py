import pulp

model = pulp.LpProblem("Beverages", pulp.LpMaximize)

# variables
lemonade = pulp.LpVariable("lemonade", lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable("fruit_jucie", lowBound=0, cat='Integer')

model += lemonade + fruit_juice

# Constraints
model += 2 * lemonade + fruit_juice <= 100, "Water_Constraint"
model += lemonade <= 50, "Sugar_Constraint"
model += lemonade <= 30, "Lemon_Juice_Constraint"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

model.solve()

print("Status:", model.status, pulp.LpStatus[model.status])
print("Lemonade:", lemonade.varValue)
print("Fruit Juice:", fruit_juice.varValue)
print(f"Total amount: {pulp.value(lemonade) + pulp.value(fruit_juice)}\n")


