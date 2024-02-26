#Create print function
def asciiPrint(asciiLocation):
    f = open(asciiLocation, "r")
    print(f.read())
    f.close()

#Validate input
def valInput(accept): # x = valInput(["yes","no"])
    while True:
        print("answer one of the following:")
        for i in accept:
            print([i])
        x = input(">>> ")
        for i in accept:
            if x == i:
                print("-"*14+"="*15+"-"*14)
                return(x)
        print("fuck off")
