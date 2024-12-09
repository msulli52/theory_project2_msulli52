
-- README -- 

Molly Sullivan 
Project 2 Extra Credit:
    even_1s.csv 
    even_1s_DTM.csv


-- OVERVIEW -- 

For extra credit on Project 2, I created even_1s.csv and even_1s_DTM.csv, which are two input tester files for 
Project 2 on tracing Turing machine behavior. These files define the language {w | w contains an even number of 1's}. 
The first file describes a nondeterministic Turing machine (NTM), while the second describes a deterministic Turing 
machine (DTM). 

I decided to create the files for this nontrivial language to help test and demonstrate the functionality of my Project 2 
implementation, including its ability to handle nondeterminism, as well as to provide examples of clear and well-structured 
automata input files for other students who may wish to use them for testing their code. Completing this has helped 
my understanding of how to traverse and trace NTM's and DTM's given different input languages as well as the formal 
definition of a Turing machine, which expands upon skills I learned for Homework 8 and 9.

I created the two autonoma files myself and I chose this language because it is simple enough to implement in both 
deterministic and nondeterministic forms, but also highlights the difference between the two models of computation.


-- FILE CONTENTS --

even_1s.csv:
- This file defines a nondeterministic Turing machine (NTM) for recognizing the language {w | w contains an even number of 1's}. 
- The machine transitions between two main states:
    - q_even: Represents the state where the input processed so far contains an even number of 1's.
    - q_odd: Represents the state where the input processed so far contains an odd number of 1's.
- Transitions are defined for every valid input character (0 and 1), as well as the blank symbol (_).
- The NTM can transition to multiple states for the same input, showcasing nondeterministic behavior.
- The machine accepts the input if it ends in the q_even state and no additional input remains, moving to the q_accept state. It rejects otherwise.

even_1s_DTM.csv:
- This file defines a deterministic Turing machine (DTM) for the same language, {w | w contains an even number of 1's}. 
- The key difference is that the DTM has a single, deterministic transition for each state and input character.
- Like the NTM, this machine transitions between q_even and q_odd based on whether the current input contains an even or odd number of 1's.
- Each transition is unique, and the machine cannot transition to multiple states for the same input.
- The DTM accepts or rejects in the same way as the NTM, but processes input deterministically.

The file contents are structured as follows:
1. Name of the machine 
2. List of states (Q)
3. List of input symbols (Σ)
4. List of tape symbols (Γ)
5. Start state 
6. Accept state 
7. Reject State
8. All transition rules 


-- HOW TO USE THE FILES -- 

To use the files, place them in the sam directory as your TM trace program (in my case, traceTM_msulli52.py). These files can then be used as input 
to the program with test strings such as 00010, 110, 0, etc. My specific program sends the output to a file and a table to see the results (some 
examples are shared below to show the output behavior).


-- EXAMPLES OF INPUT/OUTPUT BEHAVIOR ON TEST STRINGS --

Machine Name: {w | w contains an even number of 1's} - Nondeterministic
Initial String: 110
Tree Depth: 5
Total Transitions Simulated: 5
Measured nondeterminism: 1.00
String accepted in 5 steps
q_even110
1q_odd10
11q_even0
110q_even_
110_q_accept_


Machine Name: {w | w contains an even number of 1's} - Nondeterministic
Initial String: 00010
Tree Depth: 7
Total Transitions Simulated: 7
Measured nondeterminism: 1.00
String rejected in 7
q_even00010
0q_even0010
00q_even010
000q_even10
0001q_odd0
00010q_odd_
00010_q_reject_


Machine Name: {w | w contains an even number of 1's} - Nondeterministic
Initial String: 0101
Tree Depth: 6
Total Transitions Simulated: 6
Measured nondeterminism: 1.00
String accepted in 6 steps
q_even0101
0q_even101
01q_odd01
010q_odd1
0101q_even_
0101_q_accept_


Machine Name: {w | w contains an even number of 1's} - Nondeterministic
Initial String: 11111111111
Tree Depth: 13
Total Transitions Simulated: 13
Measured nondeterminism: 1.00
String rejected in 13
q_even11111111111
1q_odd1111111111
11q_even111111111
111q_odd11111111
1111q_even1111111
11111q_odd111111
111111q_even11111
1111111q_odd1111
11111111q_even111
111111111q_odd11
1111111111q_even1
11111111111q_odd_
11111111111_q_reject_


Machine Name: {w | w contains an even number of 1's} - Deterministic
Initial String: 110
Tree Depth: 5
Total Transitions Simulated: 5
Measured nondeterminism: 1.00
String accepted in 5 steps
q_even110
1q_odd10
11q_even0
110q_even_
110_q_accept_


Machine Name: {w | w contains an even number of 1's} - Deterministic
Initial String: 00010
Tree Depth: 7
Total Transitions Simulated: 7
Measured nondeterminism: 1.00
String rejected in 7
q_even00010
0q_even0010
00q_even010
000q_even10
0001q_odd0
00010q_odd_
00010_q_reject_


Machine Name: {w | w contains an even number of 1's} - Deterministic
Initial String: 0101
Tree Depth: 6
Total Transitions Simulated: 6
Measured nondeterminism: 1.00
String accepted in 6 steps
q_even0101
0q_even101
01q_odd01
010q_odd1
0101q_even_
0101_q_accept_


Machine Name: {w | w contains an even number of 1's} - Deterministic
Initial String: 11111111111
Tree Depth: 13
Total Transitions Simulated: 13
Measured nondeterminism: 1.00
String rejected in 13
q_even11111111111
1q_odd1111111111
11q_even111111111
111q_odd11111111
1111q_even1111111
11111q_odd111111
111111q_even11111
1111111q_odd1111
11111111q_even111
111111111q_odd11
1111111111q_even1
11111111111q_odd_
11111111111_q_reject_
