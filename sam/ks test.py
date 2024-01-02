num = int(input("Enter the total random numbers in sample: "))

R_sequence = []
print("Enter the random number:")
for i in range(0, num):
    random = float(input("> "))
    R_sequence.append(random)

levelSig = float(input("Enter the level of significance: "))
criticalValue = float(input(f"Enter the critical value at {levelSig} level of significance and n={num}: "))

x = []
y = []

for i in range(0, 5):
    x1 = (i+1) / num
    x.append(x1)
    y1 = i / num
    y.append(y1)

seq_iNR = []
seq_RiN = []
for i in range(0, 5):
    seq_iNR1 = x[i] - R_sequence[i]
    seq_iNR.append(round(seq_iNR1, 2))
    seq_RiN1 = R_sequence[i] - y[i]
    seq_RiN.append(round(seq_RiN1, 2))

D_plus = max(seq_iNR)
D_minus = max(seq_RiN)

sampleStatD = max(D_plus, D_minus)
print(f"Sample Statistics D is {sampleStatD}")

if sampleStatD > criticalValue:
    print("Null Hypothesis is rejected. Sample is not uniformly distributed.")
if sampleStatD <= criticalValue:
    print("Null Hypothesis is accepted. Sample is uniformly distributed.")
