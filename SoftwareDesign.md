# Software Design

### Favorite

**Lazy initialization**: I really like the idea of lazy initialization. It's not like an inherit performance gain (like doing memoization) but one that feels like it's solving a performance problem through **design**. It seems like _meta_`code` to design software with lazy initialization.

**Examples**: I can think of where lazy initialization would be useful is in OS initialization. There's no need to open something like a password user checker (not very expensive I would assume though) while the laptop is loading (running BIOS). This would only be needed just before the login screen loads (when the OS actually loads). Another example is to not calculate the next position for a cell system until the `step()` function is called.

### Anti-Pattern

An anti-pattern is spaghetti code / not modularizing `code`. I came across this during one of the backend weeks, I believe it was SQL. I had a bunch of code in `server.js`, all the routes, controller logic, and validation. I was able to make a lot of modules, ones for each "type" of object (as opposed to MVC), such as `BlogPosts`, `Users`, each in their own `dir` with route handling, controller logic (db calls), as well as a validation folder/file.

Something that I did notice though, was that I tried to modularize too much and my `routes` file just had calls to another file. However, I decided to just put all the `res.send` in that `routes` folder instead of another file called something like `routeLogic`.
