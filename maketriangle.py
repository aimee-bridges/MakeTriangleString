
#Function to build triangle with 5 rows of *

def makeTriangle():
    #empty string to store triangle
    triangle = "" 

    #Loop from 1 to 5
    for i in range(1,6):
        #add i stars and newline
        triangle += "*" * i + "\n"

    #return complete triangle to string
    return triangle

#print triangle
print(makeTriangle())