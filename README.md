# GetCoinState
The function accepts the initial state of a coin 'state' and number of times it is flipped 'n', as input. Implement the function to determine the final state of the coin after it has been flipped n A coin can be in either of the two states, headsH) or tailsT). Flipping the coin means reversing its state i.e. if it is currently in heads state, after flipping it will be in tails state. You are given a function, char GetCoinState(char state, int n);
times from the given initial state. Return the upper case character 'H' or 'T' if your answer is heads or tails respectively.


Assumption: n >= 0


Example:


Input:


T
10


Output:


T


Explanation: The coin is initially in tails state, and is flipped 10 times, after which it is again in the same state, hence the output is T.


Example:


Input:


T
5


Output:

H


Explanation: The coin is initially in tails state, and is flipped 5 times, after which it is in the heads state, hence the output is H.


Sample input

H
19
Sample Output

T
Instructions :
﻿﻿This is a template based question, DO NOT write the "main" function.
﻿﻿Your code is judged by an automated system, do not write any additional welcome/greeting messages.
﻿﻿"Save and Test" only checks for basic test cases, more rigorous cases will be used to judge your code while scoring.
﻿﻿Additional score will be given for writing optimized code both in terms of memory and execution time.
