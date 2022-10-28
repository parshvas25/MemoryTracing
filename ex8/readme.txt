Simple Loop:
Total Instructions: 120377
Total Data: 70138

The instruction that is being accessed the most is maloc, since we are creating space on the heap for 1000 * size of struct which holds an array of 128 doubles.

The data ths is being accessed the most is space on the stack through the for loop, since this is being called 10 000 times, we are making several calls to access data within a certain page

Repeat Loop:
Total Instructions: 662185
Total Data: 150731

The instruction that is being accessed the most is random, since we are calling this several times outside the loop, then once each iteration of the loop

The data that is being accessed the most is our data struct. It is being accessed in multiple loops