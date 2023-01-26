# Recursive functions II

## Description

In this exercises, we will focus on recursive functions.

*In each function created throughout these exercises the body of the function must contain a **dosctring** (a first line with a string explaining what the function does).*

##

## Tasks

###

### Task 1:

Create a recursive function named `sum_series` that takes a single argument as an integer and returns the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).

Then, use the following test cases:

```
print(sum_series(7))
print(sum_series(8))
print(sum_series(15))
```

- Your result should look like this:

```
16
20
64
```


###

### Task 2: Recursion with return and instructions after return (non tail-recursive)

Create a recursive function named `drill_sum` that takes a single argument as a list that will contain elements that are either integers or lists. These lists may, in turn, include integers or new lists. The depth of the hierarchy of lists does not have a limit.

Then, use the following test cases:

```
test_data1 = [
    1,
    [1, 2],
    [1, [2, 3]],
    [1, [2, [3, 4]]],
    [1, [2, [3, [4, 5]]]],
]
test_data2 = [
    [1, [[2, 6], [3, 4]]],
    [[5, 6, [7, 8]], [2, [3, [4, 5]]]],
    [1, [2, 3]],
    [1, 2],
    1,
]
print(drill_sum(test_data1))
print(drill_sum(test_data2))
```

- Your result should look like this:

```
35
66
```


###

### Task 3:

Create a recursive function named `count_pages` that will count the amount of pages in a website. Takes a single argument as a list of pages, defined as dictionaries that may have two keys: `title` and `pages`.

The first is the title of the page and the second is another list with the same kind of dictionaries (again with `title` and, possibly, `pages`). The tree of pages has no depth limitations.

If a page dictionary has no key `pages` it means it has no further child pages, but all the pages, including those with children, count as a page.

You can use the following test case:

```
test_data1 = [
    {
        "title": "Home",
        "pages": [
            {
                "title": "About",
                "pages": [
                    {
                        "title": "The company"
                    },
                    {
                        "title": "Our services"
                    },
                    {
                        "title": "Our products"
                    },
                    {
                        "title": "Our deliveries",
                        "pages": [
                            {
                                "title": "National"
                            },
                            {
                                "title": "International"
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Shop",
                "pages": [
                    {
                        "title": "Browse all"
                    },
                    {
                        "title": "Categories"
                    }
                ]
            },
            {
                "title": "My account",
                "pages": [
                    {
                        "title": "Settings"
                    },
                    {
                        "title": "Edit profile"
                    },
                    {
                        "title": "My transactions"
                    }
                ]
            }
        ]
    }
]
print(count_pages(test_data1))
```

- Your result should look like this:

```
15
```
