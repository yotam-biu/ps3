# Python Exercises: Edge Cases and Approximate π

## Overview
This assignment consists of two separate exercises that will challenge you to think critically about edge cases in programming and implement a mathematical approximation of π.

---

## Problem 1: Handling Edge Cases
### File: `edge_case_exercise.py`

You are given a function `move()` that simulates the movement of a pig (represented by `1`) across a list of zeros. The function takes two parameters:
1. **`my_list`**: A list of zeros with one `1`, indicating the pig's current position.
2. **`direction`**: A string (`'left'` or `'right'`) specifying the direction of movement.

The function should:
- Move the `1` to the left or right.
- Handle edge cases where moving the `1` would push it out of the list by leaving it in its current position.

### Example:
```python
move([0, 0, 0, 1, 0], 'right')  # Output: [0, 0, 0, 0, 1]
move([0, 1, 0, 0, 0], 'left')   # Output: [1, 0, 0, 0, 0]
move([1, 0, 0, 0, 0], 'left')   # Output: [1, 0, 0, 0, 0]
