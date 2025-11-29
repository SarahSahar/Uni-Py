from methods import *

# capitalize
print(my_capitalize("sara sahar"))

# casefold
print(my_casefold("SaRa SaHaR"))

# count
print(my_count("sarasahar", "sa"))

# endswith
print(my_endswith("sahar.txt", ".txt"))

# find
print(my_find("sahar and sara", "sara"))

# index
print(my_index("sahar and sepideh", "sepideh"))

# isdigit
print(my_isdigit("24680"))
print(my_isdigit("24a68"))

# islower
print(my_islower("sara"))
print(my_islower("Sara"))

# isupper
print(my_isupper("HASTI"))
print(my_isupper("HaSTi"))

# strip
print(f"'{my_strip('   sahar   ')}'")

# replace
print(my_replace("sara sahar sara", "sara", "setareh"))

# rsplit
print(my_rsplit("sara,sahar,hasti", ","))

# lsplit
print(my_lsplit("sara,sahar,hasti", ","))

# swapcase
print(my_swapcase("Setareh Sahar Is Nice"))