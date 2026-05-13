# Description: This script practices using lambda functions and multipliers

#  doubler
doubler = lambda n: n * 2

#  Test doubler
print("=== Doubler ===")
print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

#  tripler
tripler = lambda n: n * 3

print("\n=== Tripler ===")
print(tripler(8))
print(tripler(-4))
print(tripler('banana'))

#  multiplier() function
def multiplier(x):
    return lambda n: n * x

quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler  = multiplier(6)
septupler  = multiplier(7)
octupler   = multiplier(8)
nonupler   = multiplier(9)
decupler   = multiplier(10)

# Print each multiplier
print("\n=== Multipliers 4-10 ===")
print(f"quadrupler(5) = {quadrupler(5)}")
print(f"quintupler(5) = {quintupler(5)}")
print(f"sextupler(5)  = {sextupler(5)}")
print(f"septupler(5)  = {septupler(5)}")
print(f"octupler(5)   = {octupler(5)}")
print(f"nonupler(5)   = {nonupler(5)}")
print(f"decupler(5)   = {decupler(5)}")
