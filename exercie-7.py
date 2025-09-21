name = (input("Type your name ")).lower()
lover_name = (input("Type your lover name ")).lower()

l = lover_name.count("l")
o = lover_name.count("o")
v = lover_name.count("v")
e = lover_name.count("e")

nl = name.count("l")
no = name.count("o")
nv = name.count("v")
ne = name.count("e")

tl = lover_name.count("t")
to = lover_name.count("r")
tv = lover_name.count("u")
te = lover_name.count("e")

tnl = name.count("t")
tno = name.count("r")
tnv = name.count("u")
tne = name.count("e")

true_num = tl + to + tv + te + tnl + tno + tnv + tne
love_num = l + o + v + e + nl + no + nv + ne



print(f"you love score is: {true_num}{love_num}%")