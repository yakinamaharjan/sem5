import random

num = int(input("Enter the total no. of random numbers: "))
random_sequence = []
for i in range(0, num):
    rand = random.random()
    random_sequence.append(round(rand, 2))

print(random_sequence)

number_class = int(input("Enter the no. of classes: "))
expected_freq = num / number_class
observed_freq = []

# Calculating Observed Frequency
x = 0.0
for i in range(0, number_class):
    count = 0
    for j in random_sequence:
        if (j >= x) and (j < x+0.1):
            count = count + 1
    observed_freq.append(count)
    x = x + 0.1
print("Observed Frequencies are: ", observed_freq)

# Calculating Sample Statistics chi-square
sample_chi = 0
for i in range(0, number_class):
    y = ((observed_freq[i] - expected_freq)**2) / expected_freq
    sample_chi = sample_chi + y

print("Sample Statistics is: ", round(sample_chi, 3))

levelSig = float(input("Enter the level of significance: "))
critical_chi = float(input(f"Enter the critical value at {levelSig} level of significance and df=n-1={number_class-1}: "))

if sample_chi <= critical_chi:
    print("Null Hypothesis is accepted. Sample is uniformly distributed.")
else:
    print("Null Hypothesis is rejected. Sample is not uniformly distributed.")


