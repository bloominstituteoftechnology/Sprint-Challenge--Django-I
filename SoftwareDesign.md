# Your favorite software design pattern you learned this week, why, and a situation you think it'd be useful

Though I wouldn't consider this to be a `favorite`, I do enjoy working with the Observer Pattern. This is a pattern that operates by having an object, called the subject, which oversees all of it's dependents, called observers. Whenever the subject is altered, all of it's observers are informed and updated. 

This is the same pattern followed in the creation of React applications, whereby state is declared and props are passed around. I find this method to be clear and easy to work with. It makes managing an applications' data flow more simple, while also providing a level of organization conducive to production applications. Such a design pattern is especially useful when dealing with an application that has a lot of moving parts, especially of those moving parts share views.

    - A software design anti-pattern that you've run into, what happened, and what you did to fix the situation

On the same line of experience, a God Object is a potential anti-pattern that I've had to avoid in the past. Due to initial convenience it can be fairly easy to over populate a primary object with too many functions. Especially in the early days of using React, this was an issue that would from time to time begin to form. The fix was to evaluate the powers of a certain object, and if something wasn't directly relevant, to export those functions into new components of their own, thereby limiting the omniscience of one particular "primary" object.