# Emerging Technology Tasks
# Sqrt2
### Square root of 2 in Python
## Introduction
As part of our Emerging Technologies module in Final Year we were assigned this task:
- Write a Python function called sqrt2 that calculates and prints to the screen the square root of 2 to 100 decimal places. 
- Your code should not depend on any module from the standard library or otherwise. 
- You should research the task first and include references and a description of your algorithm.
<br/>
This is an interesting task as finding a square root in code is made quite simple through libraries e.g. [Java.lang.Math.sqrt()Method](https://www.geeksforgeeks.org/java-sqrt-method-examples/) but thinking of my own algorithm to find the square root of 2 will be challenging and I feel some research will be required before I can develop an accurate square root of 2 to 100 decimal places.

## Research
I first got an idea of what the square root of 2 actually was, so I calculated this by using Java's Math package, just to get a guage of what I'm aiming for (as seen in references). A square root graph also gave a good depiction of what to expect, I've placed the one I used in the references section. I could tell from all this that I could expect the answer to be around **1.4142135623730950488016887242096980785696718753769480731766797379907324784621**. I found a useful resource on [Medium.com](https://medium.com/@surajregmi/how-to-calculate-the-square-root-of-a-number-newton-raphson-method-f8007714f64/) which explained how to calculate the square root of a number using the newton raphson method where you:<br/>
While this first algorithm worked, it only returned 52 decimal palces and I had to conduct further research to improve my algorithm.
Since I couldn't format the number to print out to 2 decimal places I decided it'd be better to just get the decimal values as a whole number. This allows me to achieve 100 decimal places.
I found that a googol value is 1 followed by 100 zeros, which is perfect as that's how many decimal places I required.

## Development
My first algorithm did the following:
1. Take a reasonable guess(approximate root for the square root.
2. Add the approximate root with the original number divided by the approximate root and divide by 2.
 **x_i := (x_i + n / x_i) / 2 **
3. Continue step 2 until the difference in the approximate root along the iterations is less than the desired value (or precision value).
4. The approximate root is the square root we want.
# Development part 2
This method worked but however it only returned a value as far as 52 decimal places and thus, I had to go back to the drawing board and come up with a different approach to this problem. After further research I implemented the following:
1. I got the decimal value of 2*google, then I put that googol to the power of 2 in order to move the numbers to the left hand side of the decimal place so that I can output it. [Googol](https://stackoverflow.com/questions/34150400/how-to-enter-a-googol-in-python). I had first tried using the googol value, blue I soon realized that this didn't return the number I was looking for.
2. I then created a while loop which ran until the 'a' value was equal to the 'b' value. This first populates a with b, then uses b to make a guess at the square root of 2 by getting a floor division to receive the integers we want and not unwanted decimal format and then bit shifting the number by 1 place to the right. Bit shifts simply move the number to the right by a specified number of spaces. By doing this, we will run the while loop until we receive the same guess twice consecutively. Then you exit the while loop with the correct value for the square root of 2 (without the decimal place).
3. Get the value of the numbers to the right of the decimal place by taking (b- 10 to the power of 100) After this I simply return '1.%d' number 1 in int form followed by the finalVal which are all the numbers to the right of the decimal place

## Conclusion
My sqrt2 function appropriately returns an accurate figure for the square root of 2 which is what I was tasked to do. There is potential for re-use as you could easily implement a sqrt() function that returns square root of many numbers, I've even included a possible implementation of this as a comment near the bottom of my function. All and all this project improved my mathematical skill as well as my python programming skills. I tried to avoid returning this value as a string and I succeeded in this which I was quite happy with in the end.
**e.g.  # leftNum = int((b - finalVal)/GOOGOL) **

## References
*Newton-Raphson Method*
[NewtonMethod](https://medium.com/@surajregmi/how-to-calculate-the-square-root-of-a-number-newton-raphson-method-f8007714f64)
<br/>
*Square Root Graph*
[sqrtGraph](https://dr282zn36sxxg.cloudfront.net/datastreams/f-d%3A8c5c6810c1b36f67c852caebac576cca1ae2d3f6ad6981b8453f350d%2BIMAGE_TINY%2BIMAGE_TINY.1)
<br/>
*Python Bitwise operators*
[operators](https://wiki.python.org/moin/BitwiseOperators)
[operators2](https://www.tutorialspoint.com/python/bitwise_operators_example.html)
<br/>
*Python floor division*
[floorDiv](https://python-reference.readthedocs.io/en/latest/docs/operators/floor_division.html)
<br/>
*Nasa square root*
[nasa](https://apod.nasa.gov/htmltest/gifcity/sqrt2.1mil)
<br/>

# Using scipy.stats to verify this value of a given table and calculate the associated p value
### Chi squared testing in python

## Introduction
As part of our Emerging Technologies module in Final Year my next task was:
- Use scipy.stats to verify this value and calculate the associated p value.
- Include a short note with references justifying your analysis in a markdown cell.
<br/>
This task should be relatively straight forward as it shares some characterists to the t-test labs I was doing as part of the module.

## Research
Since we were using scipy.stats, which was new to me, I went and read into the [scipy.stats documentation](https://docs.scipy.org/doc/scipy/reference/stats.html). I found that [scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html) was a module which contains a lot of probability distributions as well as statistical functions, which is ideal for the completion of this task. Inside [scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html) I found a function called [scipy.stats.chi2contingency](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html) which is a chi-square test that checks the independence of variables in a contingency table. This is exactly what was requested in the lab.

## Development
I first imported the scipy.stats module as requested and then created 3 array's containing the values of white collar, blue collar and no collar. Once I had these, I put them into a 2 dimensional array which can be used as a perameter for the stats.chi2.contingency function. 
I then populate V, p, dof and expected values by calling the calling the stats.chi2.contingency function on my 2-dimensional array, this function does all the work and populates the variables with the relevant values. I then output these values to the screen in a user-friendly format and added my own evaluation in the markdown cell below the code.

## Conclusion
The null hypothesis of the table we were given stated that "each person's neighbourhood of residence is independent of the person's occupational classification". My chi squared test came back with a p value which was less than .001, this is lower than the significance level and thus leads me to reject the hypothesis. This was somewhat predictable as there a visable corrolation between neighborhood of residence and occupational classification. The most confusing part of this project for me was understanding what exactly the chi square test was doing and understanding what the values meant for my conclusion. Thankfully with enough research I believe I was able to grasp a proper understanding of everything.

## References
*stats.chi2.contingency*
[chi2contingency](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html)
<br/>
*Python 2D Arrays*
[2DArrPython](https://www.tutorialspoint.com/python_data_structure/python_2darray.htm)
<br/>
*Chi Square wiki*
[ChiSquareWiki](https://en.wikipedia.org/w/index.php?title=Chi-squared_test&oldid=983024096)
<br/>
*The Chi Square Test*
[ChiSquareTest](https://www.bmj.com/about-bmj/resources-readers/publications/statistics-square-one/8-chi-squared-tests)
<br/>
