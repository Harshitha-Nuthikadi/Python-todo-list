# the continue statement makes Python skip the rest of the loop body and go to the next number.
for num in range(1, 11):
    if num % 3 == 0:
        continue  # Skip this number and move to the next iteration
    print(num)
