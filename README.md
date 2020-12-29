# Generating_Syntatically_correct_program_python
This program creates a random "syntactically" correct program


To understand program, we must understand the difference between a syntatically correct program versus and semantically correct program.

When a program is "syntatically" correct, it mean that it follows the general rule of the program's grammer. In english language, we are taught to 
capitalize the first letter in the sentence, have a noun and a verb followed with the noun, and end the entire sentence with a punchuation. Programming 
is no difference, we still have to follow the rules of grammer that is present within the programs syntax.
    
      A sentence that is syntatically correct:
          The hamburger tastes good.
          
      A program that is syntatically correct (C++)
            #include <iostream>
             using namespace std;
             
            int main() {
                cout << "Hello world " << endl;
             }
             
When a program is "semantically" correct translates to everything in the program makes logically sense and there is no error. Going back to grade school,
we were taught that 2 + 2 has to equal 4, and it is valid. Programming follows through a similar position where everything in the program haas to make logical
sence. In C++, we have to declare the necessary libraries, have a main with a single well-defined entry point and a single well-defined exit point. 

A program can be syntatically correct, but not semantically correct; however, it will not run and often throw an error.
    For example:
          An english sentence that is syntatically correct, but not semantically correct is:
              "The Car's color is hamburger "
              " The wrestling tournament was pancakes "
              
            Syntatically, these sentances are correct, but semantically they are not 
 Here is a program that generates a random syntatically correct program.
