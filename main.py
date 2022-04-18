#cmd = """out test
#out hi"""

import time
import json
import importlib

with open("config.json", 'r') as c:
  config = json.load(c)

with open(config["script"] + ".armt", "r") as f:
  cmd = f.read()

outs = []

acc = ""
Int = 0

nextL = False

lineNum = 0

lines = cmd.split("\n")

vars = {}

#libVars = {}

def out(s):
  
  #global outs
  #outs.append(s)
  """
  if r == "str":
    #outs.append(s)
    print(s)
  if r == "sys":
    if s == "acc":
      #outs.append(acc)
      print(acc)
    if s == "int":
      #outs.append(Int)
      print(Int)
  """
  if s == "int":
    print(Int)
    return
  elif s == "acc":
    print(acc)
    return
  for i in vars:
    if i == s:
      print(vars[s][1])
      return
  if s[0] == "^":
    try:
      int(s[1:len(s)])
    except:
      print(f"ERROR ({lineNum + 1}): Put string as int")
      exit()
    print(s[1:len(s)])
    return
  elif s[0] == "*":
    print(s[1:len(s)])
    return
  else:
    print(f"ERROR ({lineNum}): UNKNOWN (108)")

def var(r, s):
  #print("t")
  global acc, Int
  if r == "acc":
    acc = s
  if r == "int":
    try:
      Int = int(s)
    except ValueError:
      #raise ValueError("Tried to convert string to int. Correct usage: var register int/string (Depends on variable)")
      print(f"ERROR ({lineNum + 1}): Tried to convert string to int. Int register has an int value")
      exit()

def add(n):
  global Int
  if n == "int":
    Int += Int
    return
  try:
    Int += int(n)
  except ValueError:
    print(f"ERROR ({lineNum + 1}): Tried to convert string to int. Add command takes int")
    exit()

def sub(n):
  global Int
  if n == "int":
    Int -= Int
    return
  try:
    Int -= int(n)
  except ValueError:
    print(f"ERROR ({lineNum + 1}): Tried to convert string to int. Sub command takes int")
    exit()

def mul(n):
  global Int
  if n == "int":
    Int *= Int
    return
  try:
    Int *= int(n)
  except ValueError:
    print(f"ERROR ({lineNum + 1}): Tried to convert string to int. Mul command takes int")
    exit()

def div(n):
  global Int
  if n == "int":
    Int /= Int
    return
  try:
    Int /= int(n)
  except ValueError:
    print(f"ERROR ({lineNum + 1}): Tried to convert string to int. Div command takes int")
    exit()

#def hello():
#  global outs
#  outs.append("Hello, world!")

def If(A, r, B, l):
  global acc
  if A == "int":
    a = str(Int)
  elif A == "acc":
    a = acc
  else:
    a = A
    
  if B == "int":
    b = str(Int)
  elif B == "acc":
    b = acc
  else:
    b = B
    
  if r == "==":
    if a == b:
      #acc = "true"
      run(lines[int(l)-1])
  if r == ">":
    if int(a) > int(b):
      run(lines[int(l)-1])
  if r == ">=":
    if int(a) >= int(b):
      run(lines[int(l)-1])
  if r == "<=":
    if int(a) <= int(b):
      run(lines[int(l)-1])
  if r == "<":
    if int(a) < int(b):
      run(lines[int(l)-1])
  if r == "!=":
    if int(a) != int(b):
      run(lines[int(l)-1])
def nex():
  global nextL
  nextL = True

def noOp():
  pass

def jmp(n):
  global lineNum
  lineNum = int(n) - 1

def delay(n):
  time.sleep(int(n))

def Var(n, t, v):
  global vars
  vars[n] = [t, v]

def run(l):
  #print(l)
  a = l.split(" ")
  if a[0] != "#":
    if cmds[a[0]][1] != len(a) - 1:
      print(f"ERROR ({lineNum + 1}): Not enough arguments or too much arguments")
      exit()
  #print("Hi")
  if cmds[a[0]][1] == 0:
    cmds[a[0]][0]()
  if cmds[a[0]][1] == 1:
    cmds[a[0]][0](a[1])
  if cmds[a[0]][1] == 2:
    cmds[a[0]][0](a[1], a[2])
  if cmds[a[0]][1] == 3:
    cmds[a[0]][0](a[1], a[2], a[3])
  if cmds[a[0]][1] == 4:
    cmds[a[0]][0](a[1], a[2], a[3], a[4])
  
cmds = {"out" : [out, 1], "reg" : [var, 2], "add" : [add, 1], "sub" : [sub, 1], "mul" : [mul, 1], "div" : [div, 1], "if" : [If, 4], "nex" : [nex, 0], "" : [noOp, 0], "noop" : [noOp, 0], "#" : [noOp, 0], "jmp" : [jmp, 1], "wait" : [delay, 1], "var" : [Var, 3]}

for m in config["libraries"]:
  mc = importlib.import_module(m)
  for i in mc.Cmds:
    cmds[i] = mc.Cmds[i]

#print(cmds)
    
#for line in lines:
while True:
  if lineNum == len(lines):
    break
  if nextL:
    nextL = False
  else:
    run(lines[lineNum])

  
  lineNum += 1
  

for i in outs:
  print(i)