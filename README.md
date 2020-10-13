# Sqrt2
## Square root of 2 in Python

# Introduction
As part of our Emerging Technologies module in Final Year we were assigned this task:
- Write a Python function called sqrt2 that calculates and prints to the screen the square root of 2 to 100 decimal places. 
- Your code should not depend on any module from the standard library or otherwise. 
- You should research the task first and include references and a description of your algorithm.
<br/>
This is an interesting task as finding a square root in code is made quite simple through libraries e.g. [Java.lang.Math.sqrt() Method](https://www.geeksforgeeks.org/java-sqrt-method-examples/), but thinking of my own algorithm to find the square root of 2 will be challenging and I feel some research will be required before I can develop an accurate square root of 2 to 100 decimal places.

# Research
I first got an idea of what the square root of 2 actually was, so I calculated this by using Java's Math package, just to get a guage of what I'm aiming for (as seen in references). A square root graph also gave a good depiction of what to expect, I've placed the one I used in the references section. I could tell from all this that I could expect the answer to be around **1.4142135623730951**. I found a useful resource on [Medium.com](https://medium.com/@surajregmi/how-to-calculate-the-square-root-of-a-number-newton-raphson-method-f8007714f64/) which explained how to calculate the square root of a number using the newton raphson method where you:<br/>
1. Take a reasonable guess(approximate root for the square root.
2. Add the approximate root with the original number divided by the approximate root and divide by 2.
 **x_i := (x_i + n / x_i) / 2 **
 
3. Continue step 2 until the difference in the approximate root along the iterations is less than the desired value (or precision value).
4. The approximate root is the square root we want.

# Development


# Conclusion


# References
https://medium.com/@surajregmi/how-to-calculate-the-square-root-of-a-number-newton-raphson-method-f8007714f64
<br/>
*Square Root Graph*
![sqrtGraph](https://dr282zn36sxxg.cloudfront.net/datastreams/f-d%3A8c5c6810c1b36f67c852caebac576cca1ae2d3f6ad6981b8453f350d%2BIMAGE_TINY%2BIMAGE_TINY.1)
<br/>
*Square root calculated*
![sqrt2java](https://…/3DTest.png)
