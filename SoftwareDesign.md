My favorite design pattern that we learned about is the iterator pattern. 
It makes simple loops easy to write and follow. 
For example, if I want to loop over each character in a string,
I can do a simple `for char in my_string: ...` loop, instead of 
having to make an index variable that gets incremented and using it
to access a character in the string.
  
An anti-pattern that I have run into is Dependency Hell when trying out
Typescript. Sometimes I would try to use an npm package that didn't have any 
typedefs so the compiler would screech at me unless I casted the dependencies
to an `any` type every time I tried to use the depency. 
  
Even worse, I remember one package that I was using had been recently updated but
the typedefs had not been updated. The "fix" was to create some empty typedefs
locally that would override the old typedefs. Instead, my fix was to just stop
using Typescript on that project.