def circuit_a(A, B, C):
    X1 = not A
    X2 = B and C
    Y = X1 or X2
    return Y

# Test all combinations
for A in [True, False]:
    for B in [True, False]:
        for C in [True, False]:
            print(f"A={A}, B={B}, C={C} => Y={circuit_a(A,B,C)}")
