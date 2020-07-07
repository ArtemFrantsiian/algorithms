# Description

Insertion sort is an efficient algorithm for sorting a small number of elements.

|| Performance || Big O notation ||
| Worst-case | О(n ^ 2) |
| Best-case | O(n) |
| Average | О(n ^ 2) |

## Live Example
Insertion sort works the way many people sort a hand of playing cards.
We start with an empty left hand and the cards face down on the table.
We then remove one card at a time from the table and insert it into the correct position in the left hand.
To find the correct position for a card, we compare it with each of the cards already in the hand, from right to left.
At all times, the cards held in the left hand are sorted, and these cards were originally the top cards of the pile on the table.

## Example
![Example](static/is_example.png?raw=true)

## Pseudocode
![Pseudocode](static/pseudocode.png?raw=true)
