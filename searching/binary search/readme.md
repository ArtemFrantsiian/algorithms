# Description

Binary search is a search algorithm that finds the position of a target value within a sorted array.


| Performance | Big O notation |
| --- | --- |
| Worst-case | О(log n) |
| Best-case | O(1) |
| Average | О(log n) |

## Explanation of work
Binary search compares the target value to the middle element of the array. 
If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found. 
If the search ends with the remaining half being empty, the target is not in the array.

## Example
![Example](static/example.png?raw=true)

## Pseudocode
![Pseudocode](static/pseudocode.png?raw=true)
