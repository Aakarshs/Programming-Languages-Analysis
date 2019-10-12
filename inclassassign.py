
import sys
import argparse

def main(inputFile, eta, N):
    # Initializing variables.
    eta = float(eta)
    N = int(N)
    flag = 0
    counter = 0
    newReading = 0
    newAverage = 0
    if(eta < 0.0 or eta > 1.0):
        raise Exception("The value should be between 0 and 1") # Raise error if the eta is not between the 0 and 1
    else:
        with open(inputFile) as openObject:  # openiing file as object.
            for fileElement in openObject:   # iterating through every line.
                newReading = float(fileElement)

                if (flag == N):
                    print(counter, newReading, newAverage) # Printing the counter the new reading and the average on every N.
                    flag = 0  #setting flag to zero to reprint at the next n.

                newAverage = (eta*(newReading)) + ((1 - eta) * newAverage) # Calculating the average.
                flag += 1
                counter += 1
            print(counter, newReading, newAverage)  # output the last value


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--inputFile", help="the input file")
    parser.add_argument("-e", "--eta", help="smoothing")
    parser.add_argument("-n", "--N", help="number of iterations to print on")

    args = parser.parse_args() # Parsing command line arguments.

    if (args.inputFile == None): # Checking if input argument exists.
        newInputFile =  open("newInputFile.dat","w").write(sys.stdin.read())
        main("newInputFile.dat",args.eta, args.N)
    else:
        main(args.inputFile, float(args.eta), int(args.N))



"""
#command to run:
#python3 inclassassign.py -i ./filter/data_8000000.dat -e 0.6 -n 10000 | tail -5
#cat ./filter/data_8000000.dat | python3 inclassassign.py -e 0.6 -n 10000 | tail -5


#8000000 40.912286578493536 41.22387989728809
real    0m5.236s
user    0m5.130s
sys     0m0.083s
"""