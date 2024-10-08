[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/SkD24yV8)
# 1.1.4Spirographs

*Complete the following.*

1. Compare and contrast zero-iteration conditions and infinite loops.
A zero-iteration loop is a loop that will never execute because the condition is not met while an infinite loop is a loop that never ends because the termination condition is never met. 
2. A link to your code where you solve the following problem. Take the screen size of 800px. Create code or algorithm that always places the object(s), up to 5, in the center an equal distance from one another and from the edges of the screen.
In order to place the objects an equal distance from each other, we have to
   1. get the screen size
   2. calculate size of the objects
   3. calculate margin for spacing
   4. position the objects
![image](https://github.com/user-attachments/assets/f86d5095-7d65-4d25-89c9-1992e06bc9ba)

3. Concentric Squares -- Add a screenshot of your result and the code to create it on your repo.
![image](https://github.com/user-attachments/assets/8f77a881-6b4d-46f4-929c-9df808a810e0)

Objective: Write a Python program using the turtle module to draw a pattern of concentric squares. The pattern should be created using nested loops.

Instructions:

Setup the Turtle Environment:
Import the turtle module.
Create a turtle object.
Set the turtle speed to the fastest setting.
Draw Concentric Squares:
Use a nested loop to draw multiple squares.
The outer loop should control the number of squares.
The inner loop should draw each square.
Each square should be slightly larger than the previous one.
Customize the Pattern:
Use different colors for each square.
Ensure the squares are centered on the screen.
Example Output:

The turtle should draw a series of squares, each one larger than the last, creating a pattern of concentric squares.

Hints:

Use the penup() and pendown() methods to move the turtle without drawing.
Use the color() method to change the turtle’s color.
Use the forward() and right() methods to draw the sides of the squares.


4. Complete the steps 17, 18 and 19 from [mypltw use clever to sign on](https://pltw.read.inkling.com/a/b/5310c007377c46e28d745961310f0c2e/p/728c751a6c4145bea0ea83c5058fb9f9#44b0003a2ee14fcc9865e7bb5faec747)
![image](https://github.com/user-attachments/assets/a14a8725-bf34-4aa2-b256-1213fa1ddc35)

5. Answer to step 21
The algorithm represents a loop to draw 3 circles based on a user input.  The program will continue to draw circles as long as the user enters "y" and will stop when the user enters "n".
6. Insert a screenshot or picture of the algorithm you used for your tokenizer on the previous activity.
![image](https://github.com/user-attachments/assets/ed530b99-f9a5-421e-8967-e4aecd5a4ab8)

The above code processes the user's input to find out how many and what type of flower they want using natural language processing.  The input is tokenized using nltk, which breaks the sentence down into individual tokens after converting it to lowecase letters.  These tokens are then filtered by using stop words provided by nltk.  The final tokens are then searched through to identify the type of flower and the number of flowers by checking if the token is in the list of flowers and if the token is a digit.  If the token is a flower, it is assigned the varaible flower_name and when the digit is found, it is stored as num_flowers. 

7. Give an example of an undecidable problem, attach code.

```python
age = int(input("What is your birth year")
while (age>3000):
   age = age + 1
print(age)
```


