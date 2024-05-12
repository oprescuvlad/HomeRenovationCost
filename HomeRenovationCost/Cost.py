list_of_materials = []
list_of_costs = []

shopping = True
while shopping:
    materials = input('Enter the purchased items: ')
    cost = float(input('Enter the cost of {}: '.format(materials)))

    list_of_materials.append(materials)
    list_of_costs.append(cost)

    extra = input('Do you continue to buy more? yes/no ').lower()
    if extra != 'yes':
        break

print('This is your shopping list with costs:')

for i, (material, cost) in enumerate(zip(list_of_materials, list_of_costs), start=1):
    print('{} - {}: ${:.2f}'.format(i, material, cost))

