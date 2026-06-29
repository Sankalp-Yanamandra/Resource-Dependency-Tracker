'''Task : single country's vulnerablility to a particular strategic mineral.'''

# country specific details
country_name, mineral, domestic_production, annual_consumption = "Russia", "Coal", 508190, 310960

# calculating the deficit/surplus
degree_of_vulnerability =  annual_consumption - domestic_production

# check if deficit or surplus
# initializing a flag
is_vulnerable = None
if degree_of_vulnerability > 0:
    # deficit
    is_vulnerable = True
elif degree_of_vulnerability < 0:
    # surplus
    is_vulnerable = False
else:
    # = 0 => self-sufficient
    is_vulnerable = False

# check if mineral exists in the list
critical_minerals = "Lithium", "Cobalt", "Rare Earths"
print(f'{mineral} belongs to the list of critical minerals ? : {mineral in critical_minerals}')

# final o/p
print(f'{country_name} {mineral} {degree_of_vulnerability} kt => is vulnerable ? : {is_vulnerable}')
