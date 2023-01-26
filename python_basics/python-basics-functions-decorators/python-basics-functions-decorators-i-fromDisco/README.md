# Function decorators I

## Description

In this exercise, we will focus on the usage and definition of decorators.

*In each function created throughout these exercises the body of the function must contain a **dosctring** (a first line with a string explaining what the function does).*

##

## Tasks

###

### Task 1

Create a function named `get_html_greeting` that returns a static greeting message (i.e. Hello world).

Then create a decorator named `make_bold` that takes a function returning a string and wraps it with a `<strong>` HTML tag. Decorate `get_html_greeting` with it.

Use the following test case:

```
print(get_html_greeting())
```

- Your result should look like this:

```
<strong>Hello, World!</strong>
```

###

### Task 2

Keep the previous code and create an additional function named `get_custom_html_greeting` that requires two arguments named `first` and `last`. Decorate this function with the decorator `make_bold` and adapt it to work with both `get_html_greeting` and `get_custom_html_greeting` (both with positional and keyword arguments).

Use the following test cases:

```
print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
print(get_html_greeting())
```

- Your result should look like this:

```
<strong>Hello, James Brown!</strong>
<strong>Hello, James Brown!</strong>
<strong>Hello, World!</strong>
```

###

### Task 3

Keep the previous code and change the `get_custom_html_greeting` function so that the `<strong>` tag only wraps the full name of the person.

You will have to create another function returning the full name of the person and move the `make_bold` decorator there. Then call the `get_full_name` function from `get_custom_html_greeting`.

Additionally, create two new decorators called `make_italics` and `make_paragraph` to wrap the whole greeting HTML string with an `<em>` and a `<p>` tags.

> Attention! The `<p>` must be the root tag and the `<em>` tag must be inside of it.

Use the following test cases:

```
print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
```

- Your result should look like this:

```
<p><em>Hello, <strong>James Brown</strong>!</em></p>
<p><em>Hello, <strong>James Brown</strong>!</em></p>
```

###

### Task 4

Now remove all the decorators and keep everything else. Create a unique decorator named `wrap_with` that will let us wrap a string with any tag. This tag will be indicated as a parameter of the decorator. I.e:

```
@wrap_with(tag="strong")
def get_full_name(...):
    ...
```

Use the following test cases:

```
print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
```

- Your result should look like this:

```
<p><em>Hello, <strong>James Brown</strong>!</em></p>
<p><em>Hello, <strong>James Brown</strong>!</em></p>
```
