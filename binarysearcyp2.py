# Let's call an array A a mountain if the following properties hold:
# 1. A.length >= 3
# 2. There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i - 1] < A[i] > A[i+1] > ...> A[A.length - 1]

# Given that an array that is definitely a mountain, return any i such that A[0] < A[1] < ...A[i-1] < A[i] > A[i+1] ...> A[A.length- 1]
# Example [0, 1, 0] output 1
# Example two [0, 2, 1, 0] output 1
# Note 1. 3 <= A.length <= 10000
# 2. 0 <= A[i] <= 10^6
# 3. A is a mountain as defined above