# Armtal (A custom assembly like language.)

### Note that this is not the final version, this is just V2.

## How to write a script
### Making a script
Make a new file and end it with **.armt**. Go in the config.json and change the **script** variable's value to the name of your script.
### Running a script
If you wrote a script, just run the compiler script and it will run.

---
## Instaling or writing a library
### Writing a library
Make a python script and create all your functions. Make a dictionary called **Cmds**. The name of each element is what you want it to be in the script. The value should be a list. The first thing in the list is the function. The second thing is how many arguments your command takes.

### Installing a library
It is very easy. Just put the python file in the same folder as the compiler. Go into the config.json file and add the name of it to the **libraries** list.

## Program examples
### Hello World
    out *Hello,world!
    # Spaces are not allowed when outputting a string
    
### Counting
    # This program counts up
    add 1
    out int
    jmp 1

## All Commands
### out s
Output s

### reg r s
Sets the register of r with the value of s.

### add/mul/sub/div n
Does the action you chose with int and n

### if a r b l
If a r (for example ==) b, run line l

### nex
Don't run the next line

### jmp l
Jumps to line l

### wait n
Waits for n seconds

### noop
Does nothing

### \#
A comment (doesn't do anything)

### var n t v
Make\set a variable named n with the type of t with the value of v.