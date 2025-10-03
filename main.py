# Starter code for CSIS110 Lab 4

# Add appropriate comments...such as your name, the date...

# XOR simulation
def XOR():
    # get inputs and echo them to user 
    # (don't change these 6 lines)
    A = int(input("Please enter 1 or 0 for A: "))
    B = int(input("Please enter 1 or 0 for B: "))
    print( "A is:  " ) 
    print( A )
    print( "B is:  " ) 
    print( B )

  
    # *** Fix the conditions in the if statements 
    # below so that they do the following:  *** 
    # If (A XOR B) is true, the word "TRUE" is printed
    # If (A XOR B) is false, then "FALSE" is printed
    print ( "The result is", end=" ")
    if (A == 1):
        print( "TRUE" )
    if (A == 0) and (B == 0):
        print( "FALSE" )


# Function definitions above
############################
# Test code below



