# generalTowerOfHanoi
An implementation of cp-sat solver for generalized tower of hanoi

## Tower of Hanoi Problem
- We have 3 rods, and N number of disc surrounds the first rod. 
- The disc can only be arrange from larger to smaller diameters from below to top.
- At a time, only the top disc can be moved from one rod to other.
- The goal is to move all the disc from first rod to second rod.

 It is known that the best algorithm takes 2^N -1 steps, for this version of the problem.

 ## Generalized Tower of Hanoi
- We have K rods, and N number of disc surrounds the first rod. 
- The disc can only be arrange from larger to smaller diameters from below to top.
- At a time, only the top disc can be moved from one rod to other.
- The goal is to move all the disc from first rod to second rod.

This code solves the problem using the CP-SAT library. This is not the best possible implementation, but is meant to demonstrate the power to CP-sat to solve a algorithmic problem using a optimization.
In some sense this algorithm is what one would be implemented on a non-deterministic turing machine to solve the problem.
 
## Algorithm to solve generalized Tower of Hanoi.
 Only variables are:
 - NO_PILLER: int          : number of rods,
 - NO_DISC: int            : number of disc,
 - MAX_RUN_TIME : float    : maximum run time,
 At the beginning, all the discs are placed on first rod.
 At the end, we want all the disc to be on the last rod.
### Example:
 for NO_PILLER = 4,NO_DISC = 4, the solution is
 [0 1 2 3][][][]  
 [1 2 3][][][0]  
 [2 3][][1][0]  
 [3][2][1][0]  
 [3][2][0 1][]  
 [][2][0 1][3]  
 [0][2][1][3]  
 [0][][1][2 3]  
 [0][][][1 2 3]  
 [][][][0 1 2 3]  

 Each bracket [] represts a rod. 
 The number within them represent the disc, 
 where lower no. represts smaller diameter.
