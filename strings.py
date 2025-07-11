# string method
# we have a some syntax connected with string
# in this lesson we will use a more than one var

X = "i love python"

# the first syntax print(len())
# its used to count how many character in the var 

print(len(X)) # it has 13 character

# the second syntax is print(var.split())
# its used to split your var

print(X.split()) # it will split this into [i, love , python]

Y = "i-love-python"

print(Y.split("-")) #it will remove the (-)

# the third syntax is center()
# its used to put more character into your var

Z = "mahmood"

print(Z.center(15)) # spaces
print(Z.center(15, "@")) # @

#  the fourth syntax print(.count())
# its used to count how many times does the word have been repeated in the var

V = "i love you stay by me because i love very much"

print(V.count("love")) # 2 times


# you can choose where you can start counting like this print(var.count("str" , start , end)) 

print(V.count("love" , 0 ,22 )) # 1 time


# the fifth syntax us print(var.startswith())
# its used to make sure what character does the var starts

N = "i love you"


print(N.startswith("i")) # true

print(N.startswith("f")) # false

# you can choose where to start **like indexing**

print(N.startswith("e",4,9))

# the sixth suntax is print(var.endswith())
# like the startswith but with the end

S = "why do i love you"

print(S.endswith("u")) # true

print(S.endswith("y")) # false

# you can choose where to start **like startswith**


# the sevsenth syntax print(var.find())
# its used to know the index for one character

F = "hello world"

print(F.find("r")) # its 8

# you can choose where you want to start **its like indexing**

print(F.find("r", 6,9)) #its 8


# this file is about strings
# this file was made by mahmood (BLX)
# this file was made in 2025/7/11
# this file was made for educaiton perposes







