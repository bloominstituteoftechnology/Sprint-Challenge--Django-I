  Overall, while this deployment was painful, the underlying system seems powerful and I think most of the pitfalls were probably one-time mistakes.

  My biggest complaint by far about Django *and* Heroku deployment is that there's a great number of "black box" components to both. This made it hard to debug simple problems and misunderstandings I had with the new system. However, now that I've ironed those problems out I expect them to mostly stay ironed out, and the advantage is that future deployments of a similar nature should be very smooth.
  
  I can foresee potential issues with upgrades or updates taking longer than expected, because I have no way of directly viewing how they are interacting with the stack.