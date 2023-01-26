# Task - Chunk dictionary

You are given a dictionary with a unlimited number of keys. Implement a method `chunk` that takes one argument `size`.

The method should return a list of dictionaries with each dictionary holding as many keys from the original dictionary as specified with size.

## Input:

```
data = {
  'key1': 1,
  'key2': 2,
  'key3': 3,
  'key4': 4,
  'key5': 5,
  'key6': 6,
}
```

## Output:

```
> chunk(data, 2)

[
  {
    'key1': 1,
    'key2': 2,
  },
  {
    'key3': 3,
    'key4': 4,
  },
  {
    'key5': 5,
    'key6': 6,
  }
]
```
