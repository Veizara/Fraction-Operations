# Fraction-Operations
Problem Solving with Algorithms and Data Structures using Python -  1.17 Programming Exercises 
1. Implement the simple methods getNum and getDen that will return the numerator and denominator of a fraction.

2. In many ways it would be better if all fractions were maintained in lowest terms right from the start. Modify the constructor for the Fraction class so that GCD is used to reduce fractions immediately. Notice that this means the __add__ function no longer needs to reduce. Make the necessary modifications.

3. Implement the remaining simple arithmetic operators (__sub__, __mul__, and __truediv__).

4. Implement the remaining relational operators (__gt__, __ge__, __lt__, __le__, and __ne__)

5. Modify the constructor for the fraction class so that it checks to make sure that the numerator and denominator are both integers. If either is not an integer the constructor should raise an exception.

6. In the definition of fractions we assumed that negative fractions have a negative numerator and a positive denominator. Using a negative denominator would cause some of the relational operators to give incorrect results. In general, this is an unnecessary constraint. Modify the constructor to allow the user to pass a negative denominator so that all of the operators continue to work properly.

7. Implement __radd__ method.

8. Implement __iadd__ method.

