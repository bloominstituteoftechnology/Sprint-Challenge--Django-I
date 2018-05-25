## Favorite Design Pattern

The singleton design pattern is interesting to me. I don't know if it's my favorite, but it was the most interesting one I discovered this week. At first, I was a little confused about why having only one instance of an object would be useful, but it seems like a good plan for some specific instances. It seems to be used mostly in instances where the object is a shared resource. If you have multiple things accessing different instances of an object, it would be difficult to keep track of what's actually going on. An example I see a lot is that it's like a print spooler. You only want one spooler because the entire system is using it. How would the printer know what to do if there were multiple spoolers? That's why making sure that only one spooler exists to manage everything related to the spooling process is probably a good idea. 

## Anti-pattern

I am super guilty of the God Object antipattern. I tend to forget about the whole purpose of OOP and I make one class that does everything. I usually notice pretty quickly that I've done this when things my code starts to get overly complicated, and then I try to break it down from there. I would probably save myself a ton of time if I would just think about what problems I need to solve before I start coding.
