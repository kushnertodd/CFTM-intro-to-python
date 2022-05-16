import re

def print_totals(item, dict):
    keys = list(dict.keys())
    keys.sort()
    item_header = '{:17s}'.format(item)
    print(f'{item_header}  costs')
    print("-----------------  --------")
    for key in keys:
        name = key
        total = dict[key]
        print('{:17s}  ${:7.2f}'.format(name, total))
        #print(f'{name}  {total} {type(total)}')

def add_to(customers, name, services, item, cost):
    if name in customers:
        customers[name] += cost
    else:
        customers[name] = cost
    if item in services:
        services[item] += cost
    else:
        services[item] = cost

p = "(\d{2}/\d{2}/\d{4}) (\w+) (\w+) \$(\d+\.\d+) (.*)"
f = open("orders-phone.txt", "r")
customers = {}
services = {}
print('date         name                 service         cost')
print('------------ -------------------- --------------- --------')
for s in f:
    line = s.strip()
    m = re.search(p, line)
    if m:
        date = m.group(1)
        first = m.group(2)
        last = m.group(3)
        full_name = f'{last}, {first}'
        cost = m.group(4)
        cost_float = float(cost)
        service = m.group(5)
        print('{:12s} {:20s} {:15s} ${:7.2f}'.format(date, full_name, service, cost_float))
        add_to(customers, full_name, services, service, cost_float)
    else:
        print("    line is not the right format")
        print(line)
f.close()
print()
print(f'total cost for customers')
print_totals("customers", customers)
print()
print(f'total cost for services')
print_totals("services", services)
