"""
Program contains a series class designed to handle series where
both the numerator and demoninator are polynomials where every term has a coefficient
and is a power of n. The series class also attempts a pseudo-limit convergence test function
that attempts to find a b-sub-n (b_n) expression whose behvaior is similar to the main function 
at large values for n and tell whether or not we can conclude that both to a-sub-n 
(a_n) and b_n both converge or both diverge.
"""
class series(object):
    """initialization function. Takes two number lists representing coefficients"""
    def __init__(self, num_ls, denom_ls):
        # assert statement ensures the program will be terminated if the coefficient lists
        # are of different sizes
        assert len(num_ls) == len(denom_ls),\
              f"numerator coefficient list must the same size as denominator constant list"
        self.num_ls = num_ls
        self.denom_ls = denom_ls

    """method calculates the sum of the series between index N_0 and N"""
    def calc_at_N(self, N_0, N):
        total_sum = 0 #sum variable
        for n in range(N_0, N+1): #loop iteratoes through all values between N_0 and N
            sum_num = 0
            sum_denom = 0 #both store the sum of the numerator and the sum of the denominator
            for i in range(0,len(self.num_ls)):
                #                            C * n ^ i
                sum_num += self.num_ls[-(i+1)] * (n**i) 
                sum_denom += self.denom_ls[-(i+1)] * (n**i)
            total_sum += sum_num/sum_denom #adds the 
        return total_sum #returning the total sum
    
    """method returns a string with numerator and denominator formatted like an expression"""
    def visual_representation(self):
        num_string = ""
        denom_string = ""
        first_num = True #booleans store whether or both lists have added a value yet
        first_denom = True
        for i in range(len(self.num_ls)-1,-1,-1): #i is the power
            if self.num_ls[-(i+1)] != 0: #appends nothing if coeff. is 0
                if(first_num): 
                    num_string += "{}n^{}".format(self.num_ls[-(i+1)], i) #first print has no plus sign
                    first_num = False #boolean gets set to false
                else:
                    if(i != 0): #standard print
                        num_string += " + {}n^{}".format(self.num_ls[-(i+1)], i)
                    else: #makes sure to print just the coefficient if the power = 0
                        num_string += " + {}".format(self.num_ls[-(i+1)])
            if self.denom_ls[-(i+1)] != 0:
                if(first_denom):
                    denom_string += "{}n^{}".format(self.denom_ls[-(i+1)], i)
                    first_denom = False
                else:
                    if(i != 0):
                        denom_string += " + {}n^{}".format(self.denom_ls[-(i+1)], i)
                    else:
                        denom_string += " + {}".format(self.denom_ls[-(i+1)])
        return "Numerator: {}\nDenominator: {}".format(num_string,denom_string)
    
    """attempts to approximate the limit as n approaches infinity and determine
    if value passes limit convergence test"""
    def pseudolimit_test(self, N_0, big = 3000000): #big is by default 3 million
        #WARNING THIS FUNCTION IS *VERY* SLOW WITH THE DEFAULT VALUE
        num_power = 0 #stores power of the numerator
        num_C = 1 #stores leading coefficient of the numerator
        denom_pow = 0 #stores power of the denominator
        denom_C = 1 #store leading coefficient of denominator
        for i in range(0,len(self.num_ls)): #loops through numerator coeff list
            if self.num_ls[i] != 0: #stops when a non-zero coefficient is found
                num_power = (len(self.num_ls)-1) - i
                num_C = self.num_ls[i] #num_C is set to coefficient and num_power is set to the power
                break #breaks loop
        for i in range(0,len(self.denom_ls)): #repeats above w/ denominator coeff list
            if self.denom_ls[i] != 0:
                denom_pow = (len(self.denom_ls)-1) - i
                denom_C = self.denom_ls[i]
                break
        b_n_coefficient = num_C/denom_C #b-sub-n coefficient is equal to the quotient
        b_n_power = num_power - denom_pow #power of b_n is the difference
        b_n_limit = 0 #stores the value at n = big
        for n in range(1,big): #loop finds the sum at integer "big"
            b_n_limit += b_n_coefficient * (n**b_n_power)
        a_n = self.calc_at_N(N_0, big) #calls calc_at_N method to find a_n
        #prints the expression of b_n
        print("Limit test b_n: {}n^{}\n".format(b_n_coefficient, b_n_power))
        print("Value of a_n as n approaches {}:\n{}".format(big, a_n))
        print("Value of b_n as n approaches {}:\n{}".format(big, b_n_limit))
        print("Limit of a_n/b_n as n approaches infinity is approx: {}".format(a_n/b_n_limit))
        #prints conclusion of test
        if(a_n/b_n_limit > 0.1 and a_n/b_n_limit < 100): #bounds are pretty arbitrary, as limit value is not that accurate
            print("\nSince the limit as n approaches infinity is likely less than infinity and greater than 0, a_n and b_n either both converge or both diverge\n")
        elif(a_n/b_n_limit < 0.1):
            print("\nThe limit is equal to a small value, indicating the true value of the limit as n approaches infinity may be zero or negative, making the LCT inconclusive\n")
        else:
            print("\nThe limit is equal to a large value, indicating the true value of the limit as n approaches infinity may be infinity, making the LCT inconclusive\n")

# a sample main
if __name__ == "__main__":
    print("----------------------------------")
    print("HW 10.3 QUESTION 2:")
    num = [0,4,0,5] # 4n^2 + 5
    denom = [1,20,36,0] # n^3 + 20n^2 + 36n^3
    S1 = series(num, denom)
    val_at_100 = S1.calc_at_N(23,100)
    print(S1.visual_representation())
    print("Value of the series at n_0 = 23 and n_final = 100: {}".format(val_at_100))
    S1.pseudolimit_test(23)
    print("----------------------------------")
    print("HW 10.3 QUESTION 9:")
    num = [0,0,0,1,0,-3]
    denom = [1,0,0,0,0,3]
    S3 = series(num, denom)
    val_at_100 = S3.calc_at_N(1,100)
    print(S3.visual_representation())
    print("Value of the series at n_0 = 1 and n_final = 100: {}".format(val_at_100))
    S3.pseudolimit_test(1)
    print("----------------------------------")
    print("HW 10.3 QUESTION 11:")
    num = [0,0,5,14,0]
    denom = [3,0,-5,0,-22]
    S4 = series(num, denom)
    val_at_100 = S4.calc_at_N(1,100)
    print(S4.visual_representation())
    print("Value of the series at n_0 = 1 and n_final = 100: {}".format(val_at_100))
    S4.pseudolimit_test(1)
    print("----------------------------------")