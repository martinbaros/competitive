# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  case = str([int(s) for s in input().split(" ")][0] )# read a list of integers, 2 in this case
  a = ""
  b = ""
  for letter in case:
      if letter == "4":
          a+="2"
          b += "2"
      else:
          a+=letter
          b+= "0"
  print(f"Case #{i}: {int(a)} {int(b)}")
  #print("Case #{}: {} {}".format(i, case, i))
  # check out .format's specification for more formatting options
