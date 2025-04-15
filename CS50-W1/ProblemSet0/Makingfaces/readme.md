# [Making Faces](https://github.com/LaoLuoi/CS50-Python/tree/main/CS50-W1/ProblemSet0/Makingfaces)

Before there were emoji, there were [emoticons](https://en.wikipedia.org/wiki/List_of_emoticons), whereby text like `:)` was a happy face and text like `:(` was a sad face. Nowadays, programs tend to convert emoticons to emoji automatically!

In a file called `faces.py`, implement a function called convert that accepts a str as input and returns that same input with any `:)` converted to 🙂 (otherwise known as a [slightly smiling face](https://emojipedia.org/slightly-smiling-face/)) and any `:(` converted to 🙁 (otherwise known as a [slightly frowning face](https://emojipedia.org/slightly-frowning-face/)). All other text should be returned unchanged.

## Hints

- Recall that `input` returns a `str`, per docs.python.org/3/library/functions.html#input.
- Recall that a `str` comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.
- An emoji is actually just a character, so you can quote it like any `str`, a la `"😐"`. And you can copy and paste the emoji from this page into your own code as needed.

## How to Test

Here’s how to test your code manually:

- Run your program with `python faces.py`. Type `Hello :)` and press Enter. Your program should output:

```bash
Hello 🙂
```

- Run your program with `python faces.py`. Type `Goodbye :(` and press Enter. Your program should output:

```bash
Goodbye 🙁
```

- Run your program with `python faces.py`. Type `Hello :) Goodbye :(` and press Enter. Your program should output

```bash
Hello 🙂 Goodbye 🙁
```
