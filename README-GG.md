--- Introduction ---

The Gaussian Grapher is a python script utilizing python graph rendering and a clever numerical integration technique to show the Probability Density Function and output the probability of the occurrence of a specific event. Also, AI was used in project only to re-learn python syntax (I started with Python and then switched to C++) and to remind me of using '& 1' to track the odd-even polarity of a certain number.

--- The Math ---

There is nothing much to know about the graph as it is based on the standard Gaussian Distribution function but there is quite to know about the technique used to find the probability.

Because the original function represents Probability Density, it must be integrated in order to find the probability. But Liouville's Theorem states that the indefinite integral of e^(-x^2) cannot be expressed using elementary functions. But we cannot just rely on the famous gaussian integral solution because our upper limit varies. So, out of curiosity and some sort of determination, I solved it. But how? By applying the Maclaurin series for e^x. This converted the exponentiation into an infinite polynomial. Because integration has the ability to divide among individual terms and evaluate them independently, I was able to integrate the infinite polynomial and then transform it into an infinite summation: 1/sqrt(pi) sum_{n=0}^{\infty} (-1)^n / n! * u^{2n + 1} / (2n + 1) where u = (x - mu) / (sqrt(2) * sigma).

But my laptop definitely cannot do infinite sums. Thus, I terminate the summation in my code when the term's magnitude gets equal to or below my error threshold (1e-6). But the afterward terms might have a higher magnitude, right? No, as n approaches infinity, the ratio of the terms a_{n+1} / a_n approaches 0. So, the terms in the series are monotonically decreasing.

But there is another catch: How will I evaluate a integral from -ve infinity to some upper limit because I cannot evaluate the output of a infinite polynomial at infinities? For this, I have distributed the integral in two continuous evaluations, one from -ve infinity to 0 and one from 0 to the upper limit. Since we are already indirectly given by the solution of the gaussian integral that the integral from -ve infinity to 0 of e^(-x^2) is sqrt(pi)/2, I can directly divide it by outer coefficient of 1/sqrt(pi) and get a constant offset of 1/2. Thus, the entire evaluation becomes: 1/2 + sum_...

So does Liouville's Theorem fail? Actually not. This is because infinite summations are not considered elementary algebraic functions and hence they allowed me to solve the integral.

--- Conclusion ---
This was a nice, small project. I started it today and completed it today too but the math part was very very satisfying.
