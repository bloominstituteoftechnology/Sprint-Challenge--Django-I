# Software Design

## Singleton

I thought the Singleton was an interesting concept because it is considered by some to also be an anti-pattern. I can see this being really important for OOP as it would make debugging a lot easier since there _should_ only be one place to look. The concept of __state__ is also tied to this concept and is one that we have encountered already in things like React and Redux.

One of the anti-patterns I learned of is the __God Object__. I believe I ran into a similar type of of anti-pattern with my front end project in React. In this case my main component had almost all of the variables and handler functions that I would be passed down to other components. While this was fine at first as it made it easy to track down where any issues were, it started to get pretty unwieldy once we added extra functionality during the back-end project week. I actually didn't end up fixing it, but if I were to go back to this I would probably start by breaking things out into individual components and using more advanced concepts like __render props__ or the new __Context API__ if needed. If I were build the project again from scratch I would strongly consider using some kind of state management like Redux.
