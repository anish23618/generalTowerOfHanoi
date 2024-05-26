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
In some sense this algorithm is what one would implement on a non-deterministic turing machine to solve this problem.
 
