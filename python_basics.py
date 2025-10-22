# creating list of 100 random numbers
import random
print("Generating list of 100 random numbers")
r1 = []
for i in range(100):
    rand_val = random.randint(1,1000)
    r1.append(rand_val)
print(r1)

# sorting the above generated random 100 values, min to max
print("\nSorting the above generated random 100 values, min to max")
for i in range(0, len(r1), 1):
    for j in range(i+1, len(r1), 1):
        if r1[i] > r1[j]:
            r1[i], r1[j] = r1[j], r1[i]
print(r1)

# calculating avg of even and odd numbers
print("\nCalculating avg of even and odd numbers")
even = []
odd = []
for i in r1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(f"Even: {even}")
print(f"Odd: {odd}")

avg_even = round(sum(even)/len(even),2)
avg_odd = round(sum(odd)/len(odd),2)
print(f"Avg of even: {avg_even}")
print(f"Avg of odd: {avg_odd}")
