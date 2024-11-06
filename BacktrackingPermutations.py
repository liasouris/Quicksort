def permutations(n, target_permutation_index):
    # Initialize necessary arrays
    numbers = [0] * n       # Array to hold the current permutation
    included = [False] * n  # Boolean array to check if a number is included in the current permutation
    count = [0]  # Use a list to keep track of count across recursive calls

    def generate(k):
        if k == n:
            count[0] += 1  # Increment the permutation count
            if count[0] == target_permutation_index:
                print("50th permutation:", numbers)
                return True  # Stop once we reach the target permutation
        else:
            for i in range(1, n + 1):
                if not included[i - 1]:  # Check if the number i is already included
                    included[i - 1] = True
                    numbers[k] = i
                    if generate(k + 1):  # Recurse to add the next number
                        return True  # Stop recursion when target is found
                    included[i - 1] = False  # Backtrack to try other numbers
        return False

    # Start the recursive generation
    generate(0)

# Set n = 5 and find the 50th permutation
permutations(5, 100)
