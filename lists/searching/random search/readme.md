# Description

Random search is a search algorithm that finds the position of a target value using random algorithm.


## Explanation of work
Pick a random index i into A. If A\[i] = x, then we terminate; otherwise, we continue the search by picking a new
random index into A. We continue picking random indices into A until we find an
index j such that A\[j] = x or until we have checked every element of A. Note
that we pick from the whole set of indices each time, so that we may examine a
given element more than once.
