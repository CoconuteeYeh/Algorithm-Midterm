import random
import time

def linear_search(S, x):
    for i in range(len(S)):
        if S[i] == x:
            return True
    return False

def binary_search(S, x):
    low = 0
    high = len(S) - 1
    while low <= high:
        mid = (low + high) // 2
        if S[mid] == x:
            return True
        elif S[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False

def fibonacci_search(S, x):
    fib2 = 0
    fib1 = 1
    fib = fib1 + fib2
    while fib < len(S):
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2
    offset = -1
    while fib > 1:
        i = min(offset+fib2, len(S)-1)
        if S[i] < x:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif S[i] > x:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return True
    if fib1 and S[offset+1] == x:
        return True
    return False

# Set up the experiment
results = {'linear': [], 'binary': [], 'fibonacci': []}
num_trials = 5
num_iterations = 100
x = 42

# Run the experiment
for n in range(10, 1010, 10):
    for i in range(num_iterations):
        S = [random.randint(0, n*10) for j in range(n)]
        start_time = time.time()
        for j in range(num_trials):
            linear_search(S, x)
        end_time = time.time()
        results['linear'].append((n, end_time - start_time))

        S = sorted(S)
        start_time = time.time()
        for j in range(num_trials):
            binary_search(S, x)
        end_time = time.time()
        results['binary'].append((n, end_time - start_time))

        start_time = time.time()
        for j in range(num_trials):
            fibonacci_search(S, x)
        end_time = time.time()
        results['fibonacci'].append((n, end_time - start_time))

# Compute the average execution times for each algorithm
averages = {'linear': [], 'binary': [], 'fibonacci': []}
for alg in results:
    for n in range(10, 1010, 10):
        total_time = sum([t for (m, t) in results[alg] if m == n])
        avg_time = total_time / num_iterations
        averages[alg].append((n, avg_time))

# Print the results
print('n\tLinear\tBinary\tFibonacci')
for n in range(10, 1010, 10):
    print('{}\t{:.6f}\t{:.6f}\t{:.6f}'.format(n, averages['linear'][n//10-1][1], averages['binary'][n//10-1][1], averages['fibonacci'][n//10-1][1]))