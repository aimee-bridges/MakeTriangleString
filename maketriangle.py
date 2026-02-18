#function that builds a triangle with anumber of rows
def makeTriangle(num_rows):
     # Start with an empty string to store the triangle
    triangle = "" 

    # Loop from 1 up to the number of rows requested
    for i in range(1, num_rows + 1):
         # Add i stars and a newline
        triangle += "*" * i + "\n"
    # Return the completed triangle string
    return triangle  

# Example: print a triangle with 5 rows
print(makeTriangle(5))