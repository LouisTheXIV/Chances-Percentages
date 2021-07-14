# Chances and Percentages
Python program to do with percentages and chances, random generation.

# What is this?
This small program will generate a list with random values inside of it. There are 3 values, A, B, and C. The chance of A being in the list is 0.75, B chance is 0.50, C chance is 0.25, and for it to be empty is 0.50.
The chance of getting that list will be calculated for you, for example if you get all 3 values empty the chance of getting that is 0.125%, because 0.50**3 is 0.125.

# Decoding a chance into a list
When you call the generate_table() function you can pass an arguemnt if you want. That argument should be a chance, for example 0.125. Let's say we pass in 0.125 as the chance, the program will decode it into a list of values and a list of our 4 values, A, B, C, and nothing. If we pass in 0.125 then it will decode it into all 3 chances having to be 0.50.
Then it will generate the table/list of our values, so the list will either be full of B's or will be totally empty.

Make sure you pass in a valid chance otherwise it won't work! You can modify the chances as well by modifying the variables at the top of the code.
