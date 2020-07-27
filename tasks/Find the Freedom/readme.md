Find the freedom
================

A k-multiple free set is a set of integers where there is no pair of integers where one is equal to another integer multiplied by k. 
That is, there are no two integers x and y (x < y) from the set, such that y = x * k.

You're given a set of n distinct positive integers. Your task is to find the size of it's largest k-multiple free subset.

Write a function solution(n, k, l), that takes two integers n (1 ≤ n ≤ 10 ^ 5) and k (1 ≤ k ≤ 10 ^ 9) 
and list of n distinct positive integers a1, a2, ..., an (1 ≤ ai ≤ 10 ^ 9) 
and return the size of the largest k-multiple free subset of {a1, a2, ..., an}.


Test cases
==========
Your code should pass the following test case(-s).

Input: solution(6, 2, [2, 3, 6, 5, 4, 10])
Output: 3
