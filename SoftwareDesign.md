# Software Design: Patterns and Anti-Patterns

## Favorite Design Pattern
I absolutely love the idea of reusable code, so DRY stands as my current favorite design pattern, even more when it comes to OOP (though it applies to any programming paradigm). Establishing reusable code early on can save a lot of refactoring down the line, and naturally just results in more easily-read code, more maintainability (due to being able to change one thing in one spot and have that change apply everywhere it needs to, rather than having to search through and change each individual instance), and far less typing overall.

## Encountered Anti-Patterns
In complete contrast to what was stated above, the anti-pattern I've encountered most, particularly in my own code, is repetition of previously written code (WET solutions). Occasionally DRY can be difficult to stick with, especially with a new language. As an example from the Djorg project, I had attempted to write two functions within `views.py` in order to handle public bookmarks versus private bookmarks, and aside from the `form` variable, the rest of the code was identical, which is hardly the optimal solution.

Unfortunately, since I still have little to no idea what I'm doing with Django, I was unable to get this code to work at all, let alone spend any time refactoring for reusable code, and reverted back to the functional lecture code for the time being.