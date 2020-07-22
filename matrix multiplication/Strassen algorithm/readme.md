Strassen algorithm
=============
Strassen algorithm is an algorithm for matrix multiplication. It is faster than the standard matrix multiplication algorithm and is useful in practice for large matrices, but would be slower than the fastest known algorithms for extremely large matrices.

Performance
O(n<sup>lg7</sup>)

Description
===========
Let `A`, `B` be two square matrices. We want to calculate the matrix product `C` as `C = A * B`
and if the matrices A, B are not of type 2n × 2n we fill the missing rows and columns with zeros.

We partition `A`, `B` and `C` into equally sized block matrices:

![Example](static/matrices_partitioning.png?raw=true)

The Strassen algorithm defines new matrices:

![Example](static/new_matrices.png?raw=true)

only using 7 multiplications (one for each M<sub>k</sub>) instead of 8 in standard algorithm. 

We may now express the C<sub>i,j</sub> in terms of M<sub>k</sub>:

![Example](static/c.png?raw=true)

We iterate this division process `n` times (recursively) until the submatrices degenerate into numbers. The resulting product will be padded with zeroes just like `A` and `B`, and should be stripped of the corresponding rows and columns.