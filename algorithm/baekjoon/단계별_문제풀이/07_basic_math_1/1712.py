import sys

fixed_cost, variable_cost, production_cost = map(
    int, sys.stdin.readline().rstrip().split()
)
result = 0

if production_cost <= variable_cost:
    result = -1
else:
    result = fixed_cost // (production_cost - variable_cost) + 1

print(result)
