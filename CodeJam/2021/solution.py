# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  case = str([int(s) for s in input().split(" ")][0] )# read a list of integers, 2 in this case

  print("Case #{}: {} {}".format(i, case, int(b)))
  # check out .format's specification for more formatting options



#viac riadkove
