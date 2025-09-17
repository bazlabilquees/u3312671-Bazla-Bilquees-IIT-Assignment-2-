def circuit_b(P, Q, R):
    X1 = P or not Q
    X2 = Q and R
    Z = X1 and X2
    return Z

# Test all combinations
for P in [True, False]:
    for Q in [True, False]:
        for R in [True, False]:
            print(f"P={P}, Q={Q}, R={R} => Z={circuit_b(P,Q,R)}")
