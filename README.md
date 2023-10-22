# Natural Logarithm Implementation

This repository contains a Python implementation of the natural logarithm function, `ln`, from scratch. The function calculates the natural logarithm of a number using the properties of logarithms and the Taylor series.

## Functionality

The `ln` function takes two arguments: `number` and `precision`. The `number` is the input for which we want to calculate the natural logarithm, and `precision` is an optional argument that determines the number of terms in the Taylor series expansion (default is 20).

The function works by first decomposing the input number into a product of a scaling factor and a power of two using the `decomposer` function. The Taylor series is then used to calculate the natural logarithm of the scaling factor, and the natural logarithm of the power of two is added to this result.

## Results

The performance of our `ln` function is quite impressive when compared to the implementation provided by NumPy. However, the optimized version of our function demonstrates even closer alignment with NumPy’s results. This is primarily due to its superior convergence rate, which significantly enhances the accuracy of our implementation.
![WhatsApp Bild 2023-10-22 um 22 25 03_dc189d74](https://github.com/FalkAurel/natural-logarithm/assets/137809006/e54fef21-e145-4333-8240-96b9396472d6)

## Explanation

Computing the natural logarithm is no easy task. However, we can leverage algebra to our advantage, as we can express the ln in terms of an infinite series that converges. A series can be thought of as a term that changes in a very defined and predictable pattern as you approach infinity.

We start with a geometric series formula:

$$s = \sum_{n=0}^{\infty} a \cdot r^n = a + ar + ar^2 + ar^3 + ... + ar^n$$

We then transform it with the aim to solve for s:

$$s = a + r(a + ar + ar^2 + ar^3 + ... + ar^{n-1} + ...)$$

Since we have an infinite amount of terms we can rewrite s to be equal to $a + rs$, which enables us to subtract $rs$:

$$s - rs = a$$

We can now factor out s such that:

$$s(1 - r) = a$$

When we now divide both sides by $(1 - r)$ we get:

$$s = \frac{a}{1 - r}$$

For our case we can replace $a$ with $1$ and $r$ with $-x$ such that we get:

$$s = \frac{1}{1 + x}$$

The interesting property of this function is that its area under the curve from 0 to x is equal to $\ln(1 + x)$. Meaning that:

$$\ln(1 + x) = \int_{0}^{x} \frac{1}{1 + t} dt$$

Remember that you could write this integral as an infinite sum. And according to the Summenregel, we are allowed to distribute the integral and add them up later as long as the intervals are the same. Which means I can compute the integral for the first term, then the second and so on AND then add them up later.

We can generalize this to:

$$\ln(1 + x) = \sum_{n=0}^{\infty} (-1)^n \cdot \frac{x^{n+1}}{n+1}$$

The problem is our formula relies on the fact that the series converges. This is only true for $-0.5 < x < 0.5$. Luckily we can use properties of the logarithm to make things easier.

Using these properties we can now take very large inputs and divide them into small manageable chunks.

For example, to take the natural logarithm of 10 we could:

$$\ln(10) = \ln(2^5 \cdot \frac{5}{16}) = 5 \cdot \ln(2) + \ln(\frac{5}{16})$$

which in both cases gives us 2.302585093.

## Credits

I am deeply grateful to [zachartrand](https://zachartrand.github.io/SoME-3-Living/#fn:notfactorial) for the comprehensive mathematical explanations provided in his work. His clear and insightful presentation of the concepts greatly facilitated my understanding and was instrumental in the completion of this project. Thank you for sharing your knowledge with the community.

