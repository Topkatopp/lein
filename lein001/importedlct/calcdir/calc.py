from contrle import *
op=write2("write operation>> ")
n=write2("write 1 number>> ", type="int")
b=write2("write 2 number>> ", type="int")
write1(calc(f"{n}{op}{b}"))
imp("random")
from contrle import *
if n < b:
	write1(rand(n, b))
else:
	write1("you can't use a random module")
write2()