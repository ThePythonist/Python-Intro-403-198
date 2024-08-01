# Iterate through numbers from 0 to 5 using the range function
for x in range(6):
    # Check if the current value of 'x' is equal to 3 or 6
    if x == 3 or x == 6:
        # If 'x' is 3 or 6, skip to the next iteration without executing the code below
        continue
    # Print the value of 'x' with a space and without a newline (end=' ')
    print(x)
    print("-"*50)

# Print a new line after printing all numbers satisfying the condition
print("\n")
