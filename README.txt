**The following is a transcription of the project report handed in December of 2022**

-Major: 

Computer Science and Cognitive Science dual major


-Why did you choose this project:

I chose this project because I have some experience with Python and I know that it’s very popular 
with people who work with series and sequences as they relate with AI. I wanted to see if I could 
make an applicable program that can handle those sorts of calculations.


-Description:

The program itself contains a series class designed to handle series where both the numerator and
denominator are polynomials where every term of each polynomial has a coefficient and is a power of
n. The series class also attempts a pseudo-limit convergence test function that attempts to find a 
b-sub-n (b_n) expression whose behavior is similar to the main function at large values for n and 
attempts to tell whether or not we can conclude that both to a-sub-n (a_n) and b_n both converge 
or both diverge.

-Notes:
the convergence test function finds the behavior of the a_n and b_n at large values of n, with 
3 million being the default value of n. Hence, the function is pretty slow. I provided two test 
cases that are problems from the homework. Each took about 20 seconds to execute on my machine. 
When testing, the speed of the function can be changed by setting the default argument to a lower 
value:

	S1 = series([4,5,6] , [7,8,9]) #object declaration. Lists must be the same size.

	S1.pseudolimit_test(1) #default call where starting index is 1 and ending index is 3 million

	S1.psuedolimit_test(1, big = 10000) 
	#big is now set to ten thousand. The results will be less accurate, but the function will be faster
