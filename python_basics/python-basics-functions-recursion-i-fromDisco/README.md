# Recursive functions I

## Description

In this exercises, we will focus on recursive functions.

*In each function created throughout these exercises the body of the function must contain a **dosctring** (a first line with a string explaining what the function does).*

##

## Tasks
###

### Task 1: Recursion with no return (no unwinding)

Create a recursive function named `countdown` with a single integer input argument that prints a countdown starting from the given number.

Then, use the following test case:

```
countdown(5)
```

- Your result should look like this:

```
5
4
3
2
1
0
```

###

### Task 2: Recursion with return and instructions after return (non tail-recursive)

Create a recursive function named `factorial` that returns the factorial of a number (the number multiplied by every integer lower than the number and greater than 0).

Then, use the following test cases:

```
print(factorial(0))
print(factorial(1))
print(factorial(10))
```

- Your result should look like this:

```
1
1
3628800
```

###

### Task 3: Recursion with return and instructions after return (non tail-recursive)

Create a function called `harmonic_sum` that requires an integer as an argument. The function will return the harmonic sum of the integer.

The harmonic sum is the sum of reciprocals of the positive integers. The harmonical sum of 2 is:

1/1 + 1/2 = 1.5

The harmonic sum of 4 is:

1/1 + 1/2 + 1/3 + 1/4 = 2.083333333333333

Then, use the following test cases:

```
print(harmonic_sum(7))
print(harmonic_sum(4))
```

- Your result should look like this:

```
2.5928571428571425
2.083333333333333
```
