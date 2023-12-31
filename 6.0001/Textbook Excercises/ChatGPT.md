# ChatGPT Answers

## 3.2 Finger Exercise 2
Certainly! The algorithm you're describing is called the "Two Egg Problem," and it can be solved using a modified binary search approach. Here's an implementation of the algorithm in Python:

```python
def find_highest_floor():
    total_floors = 102
    safe_interval = 14  # Start with an interval of 14 floors

    # First egg - find the interval in which the egg breaks
    egg1_floor = 0
    while egg1_floor + safe_interval <= total_floors:
        if is_broken(egg1_floor + safe_interval):
            break
        egg1_floor += safe_interval
        safe_interval -= 1

    # Second egg - perform a linear search within the identified interval
    egg2_floor = egg1_floor
    while egg2_floor < egg1_floor + safe_interval:
        egg2_floor += 1
        if is_broken(egg2_floor):
            break

    return egg2_floor

def is_broken(floor):
    # Replace this function with the actual implementation of egg drop
    # It should return True if the egg breaks from the given floor, and False otherwise
    # You can simulate this with a comparison to the highest safe floor
    highest_safe_floor = 67
    return floor > highest_safe_floor

# Testing the algorithm
highest_safe_floor = find_highest_floor()
print("The highest safe floor is:", highest_safe_floor)
```

In this implementation, we start with an interval of 14 floors. The first egg is used to find the approximate interval where the egg breaks. By decreasing the interval size by 1 each time, we can reduce the number of eggs used for this phase to a maximum of 14.

Once we have a smaller interval, the second egg is used to perform a linear search within that interval. This phase requires a maximum of `safe_interval` eggs, which in this case is 14.

Note that the `is_broken()` function is a placeholder, and you'll need to replace it with the actual egg drop mechanism according to your requirements. The function should return `True` if the egg breaks from the given floor and `False` otherwise.

This implementation guarantees that at most seven eggs will be used to find the highest safe floor in the worst-case scenario.