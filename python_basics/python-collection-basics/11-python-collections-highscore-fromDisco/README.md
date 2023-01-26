# Task - Highscore

You have a list of participants as strings. This list holds title-cased names. Alongside there is a dictionary with scores, using the same names as keys with a integer as their value.

Implement a method `get_score` that takes a name as an argument, verifies it is in the list of participants and then prints the name with the score.

If the participant can't be found print a message telling that.

## Input:

```
participants = ['Brian', 'Britney', 'Ben']
scores = {
  'brian': 25,
  'britney': 80,
  'ben': 50
}

get_score('Paul')
get_score('Britney')
```

## Output:

```
Paul did not participate
Britney scored 80 points
```
