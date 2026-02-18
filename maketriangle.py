# Define a function that builds a centred pyramid-style triangle
def makeTriangle(num_rows):
 # Start with an empty string to store the final triangle
    triangle = "" 
   
    # Loop from 1 up to the number of rows requested
    for i in range(1, num_rows + 1):

        # Calculate how many spaces are needed on the left to centre the stars
        spaces = " " * (num_rows - i)

        # Calculate how many stars to print on this row (odd numbers: 1, 3, 5, ...)
        stars = "*" * (2*i - 1)

        # Add the spaces + stars + newline to the triangle string
        triangle += spaces + stars + "\n"

# Return the completed triangle string
    return triangle               

# Print a triangle with 5 rows
print(makeTriangle(5))