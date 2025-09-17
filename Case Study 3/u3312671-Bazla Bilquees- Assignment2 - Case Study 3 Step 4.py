# u3312671 Bazla Bilquees - Case Study 3 - Assignment 2
# Replace these lists with your truth-table outputs in row order A,B,C: 000,001,010,...,111
# Each element is a tuple (X, Y)
truth_a = [
    (0,0),  # A=0 B=0 C=0
    (1,0),  # A=0 B=0 C=1
    (0,1),
    (1,1),
    (0,0),
    (1,0),
    (0,1),  # example row 110
    (1,1),
]

truth_b = [
    (0,0),
    (1,0),
    (0,1),
    (1,1),
    (0,0),
    (1,0),
    (1,1),  # differs from truth_a at row index 6
    (1,1),
]

assert len(truth_a) == len(truth_b), "Both truth tables must have same length"

diffs = []
for i, (out_a, out_b) in enumerate(zip(truth_a, truth_b)):
    A = (i >> 2) & 1
    B = (i >> 1) & 1
    C = i & 1
    if out_a != out_b:
        diffs.append((i, A, B, C, out_a, out_b))

if not diffs:
    print("Equivalent: all outputs match for every input.")
else:
    print("NOT equivalent. Differences found:")
    for idx, A, B, C, out_a, out_b in diffs:
        print(f" Row {idx}: A={A} B={B} C={C}  CircuitA={out_a}  CircuitB={out_b}")
