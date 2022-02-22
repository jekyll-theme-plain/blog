---
date: 2022-02-19 07:53:26 +0000
---

I have been re-learning programming lately using C++.

After Hello World, I wrote a simple program about prime numbers.

A natural number n > 1 is prime if and only if it is not divisible by any natural number i such that 2 <= i <= n – 1. The numbers 0 and 1 are not prime.

A simple C++ program to print the primes less than or equal to 100 would be as follows:

    #include <iostream>

    // Returns whether `n` is prime.
    bool is_prime(int n) {
      if (n <= 1) {
        return false;
      }

      for (int i = 2; i < n; i++) {
        if (n % i == 0) {
          return false;
        }
      }

      return true;
    }

    int main() {
      // Prints the prime numbers less than or equal to 100.
      for (int n = 0; n <= 100; n++) {
        if (is_prime(n)) {
          std::cout << n << std::endl;
        }
      }
    }

This algorithm is called trial division, which attempts to divide n by smaller numbers.

There are some improvements that can be made to this program:

- Using using namespace std, it is possible to avoid writing std:: every time like std::cout or std::endl. This is considered bad in header files (with extensions *.h, *.hpp, etc.), but not in source files (with extensions *.cc, *.cpp, etc.).
- Using const for constants, such as is_prime‘s n argument, is a good practice, just like in JavaScript/TypeScript.
- i++ should be written as ++i. They are the same for primitives such as int, but the latter is sometimes faster in other cases. For consistency, the latter form should always be used.
unsigned int (aka unsigned) should be used instead of int.
According to Wikipedia, int can handle integers in the range [-32767, +32767], while unsigned can handle [0, 65535].
- It is controversial whether we should always use unsigned for non-negative integers such as loop counters, but in this case, we will want to handle as large an integer as possible, so we should definitely use it.
Or better yet, unsigned long long int (aka unsigned long long) should be used, which is guaranteed to handle [0, 2^64 – 1]. It is given the short name uint64_t in <cstdint>.

For main:
- For reusability, main should be factored out to “a function that returns a vector of primes less than or equal to a given natural number”.
- It should only iterate over odd numbers, since all primes except 2 are odd.

For is_prime:
- It is enough to trial divide by only the primes in [2, n – 1]. Because if n is divisible by a composite number, then it must already be divisible by its prime factor.
We can emulate it by iterating over the odd numbers in that range, if n is not even.
- It is enough to trial divide only in [2, sqrt(2)], as is well known.
I don’t know how to prove it, but I think it can be demonstrated by the following example:
Consider whether 113 is prime. It is not divisible by 2, 3, 5, or 7. Then there is no need to divide by 11. Because if 113 = 11 * x, then x < 11, so it must already divisible by a smaller prime. (Hence, 113 is prime.)
