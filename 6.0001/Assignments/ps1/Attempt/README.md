# Alternative
Attempted to solve problem set 1c with a mathematical approach.  

## logic
if a program must calculate the savings I would get for each changing value of `portion_saved`, I tried to avoid using nested while-loop for each iteration.  
if a clean cut mathematical formula can replace a while-loop, then I could avoid the inner while-loop.  

## methodology
drew out tables of income in each month, and derived equations from the pattern  

## findings
1. when a mathematical function involves sigma or recurring addition, programming cannot escape loops.  
2. some mathematical representation is better treated with conditionals (if-else). 
   1. increase in salary of (1.07 s) can be done using if-statement rather than 1.07 ** (n // 6)  
