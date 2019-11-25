# My_Coding_Exercises

The repository contains a few python scripts containing some code that can be treated as
coding exercises.

The file reverse_polish_notation.py provides functions for verifying whether an arithmetic expression in
Reverse Polish Notation (rpn) is well-formed, whether an arithmetic expression in Natural Notation (nn) is well-formed, 
functions for converting well-formed expressions from rpn to nn and vice versa and, finally, functions for computing 
values of well-formed expressions in rpn or nn. All the algorithms used for the implementation of the functions are 
based on the use of stacks. The file tests.py contains relevant unittests evidencing correctness of the functions 
mentioned above.

The file permutation_class.py contains a class for the representation of permutations. Methods implemented there allow
one to inverse and compose permutations and, moreover, to obtain the canonical cycle notation of a permutation. The file
permutations.py contains a function generating all the permutations of a given list of items.

The file fractions_and_det.py provides class for the representation of fractions and implements as methods basic 
arithmetical operations on fractions. Moreover, the det (determinant) function is defined for computing determinants of 
matrices with fractional values, whose value is a fraction as well so no rounding error is involved. The value of the
det is computed by an algorithm that transforms the initial matrix into an upper triangular matrix. The complexity of
the algorithm is O(n^2), where n is the number of rows (or columns) in the matrix.
Some functions implementing Cramer method for solving systems of linear equations are provided based on the det function.

The file L-systems.py provides generators for Lindemayer systems (aka L-systems). Such a system is an automaton that transforms
every letter (from a given alphabet) into sequence of letters according to some fixed set of production rules of the form: 
letter -> <sequence_of_letters>. The function L_deterministic_generator takes two arguments: start (initial sequence of letters)
and rules (a list of production rules) and generates successively words (sequences of letters) each of which is derived 
according to the production rules from the previous one.
The function L_random_generator represents so called stochastic L-system, where to each letter there is assigned a
set of production rules each one with a given probability (the sum of the probabilities is equal to 1). The 'rules'
parameter in the function is supposed to be a list of tuples, each tuple consisting of a sequence and its weight (instead of
direct probability - relevant probabilities are computed from the weights). The rule that is at a given moment applied
in rewriting the current word is chosen with the corresponding probability   
