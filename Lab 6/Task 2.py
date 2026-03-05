import random

def f(x):
    return -x**2 + 10*x + 5

def hill_climb():
    x = random.randint(0, 100)
    
    while True:
        current_value = f(x)
        neighbors = []

        if x - 1 >= 0:
            neighbors.append((f(x-1), x-1))
        if x + 1 <= 100:
            neighbors.append((f(x+1), x+1))

        best_value, best_x = max(neighbors, default=(current_value, x))

        if best_value > current_value:
            x = best_x
        else:
            break

    return x, f(x)

for i in range(5):
    x_max, f_max = hill_climb()
    print(f"{i+1}: x = {x_max}, f(x) = {f_max}")