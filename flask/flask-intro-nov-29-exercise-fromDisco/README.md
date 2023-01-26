Some helpful instructions:

In this exercise, explore the use of iPython. A tool for interactive computing.

Start the iPython shell by typing the following command:

```console
ipython
```

You can load scripts in the currently working directory by:

```console
%load <name of file>.py
```

Sometimes when code is loaded you have to press the `enter` key two times for it to be reflected.



# Exercise

Add support for an unknown number of arguments and make sure the data is queried
e.g. `Reminder.find(title="a", description="Loves to eat")`  should be able to find a reminder with a title and a description that match.


- You may have to use concepts like `**kwargs` or `*args`
- the search should be case insensitive **hint**: Integrate the use of `LIKE` in Postgresql
- Your SQL can query more than one column at the same time
- Change the return value to be a list of Reminder instances.

- Extra credit/harder: It should be possible to search for words that have a typo in them. For example, 
if you saved a reminder with the title: `"The book is good"` and someone were to search for `"the bok is goodd"`, this is a close result and should be returned.
Design the Google search engine!