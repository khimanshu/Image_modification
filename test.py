#Name : Himanshu
#Date : 10/17/2016
#Class and section : CS524-02
#python 3.5.2
import sys

def splitter(s,spl,ind):
	indx=[i for i,j in enumerate(s) if j==spl][ind-1]
	return [s[:indx],s[indx+1:]]



def grey_scale():

    inputf = open("cake.ppm" , "r")
    output = open ("cakemodify.ppm" , "w+")

    output.write (inputf.readline())
    output.write (inputf.readline())
    output.write (inputf.readline())

    for i in inputf.readlines():
	j = i.split()
	for k in range (0, len(j), 3):
		sum = int (int(j[k]) + int(j[k+1]) + int(j[k+2]))
		#print("sum is ",sum)
            	avg = int (sum/3)
		#print("Average is ",avg)
            	j[k] = int (avg)
            	j[k+1] = int (avg)
            	j[k+2] = int (avg)
        for k in range (0, len(j), 1):
            output.write(str(j[k]) + ' ')
        output.write('\n')
    inputf.close()
    output.close()


def negate_red():

    inputf = open("cake.ppm", "r")
    output = open("cakemodify.ppm" , "w+")

    output.write (inputf.readline())
    output.write (inputf.readline())
    output.write (inputf.readline())

    for i in inputf.readlines():
            j = i.split()
            for k in range (0, len(j), 3):
                j[k] = int(255 - int(j[k]))
                j[k+1] = j[k+1]
                j[k+2] = j[k+2]
            for k in range (0, len(j), 1):
                output.write(str(j[k]) + ' ')
                output.write('\n')
    inputf.close()
    output.close()


def negate_green():

    inputf = open("cake.ppm", "r")
    output = open ("cakemodify.ppm" , "w+")

    output.write (inputf.readline())
    output.write (inputf.readline())
    output.write (inputf.readline())

    for i in inputf.readlines():
            j = i.split()
            for k in range (0, len(j), 3):
                j[k] = j[k]
                j[k+1] = int (255 - int (j[k+1]))
                j[k+2] = j[k+2]
            for k in range (0, len(j), 1):
                output.write(str(j[k]) + ' ')
                output.write('\n')
    inputf.close()
    output.close()


def negate_blue():

    inputf = open("cake.ppm", "r")
    output = open("cakemodify.ppm", "w+")

    output.write(inputf.readline())
    output.write(inputf.readline())
    output.write(inputf.readline())
    for i in inputf.readlines():
            j = i.split()
    	    for k in range(0, len(j), 3):
            	j[k] = j[k]
            	j[k + 1] = j[k + 1]
            	j[k + 2] = int (255 - int (j[k + 2]))
            for k in range(0, len(j), 1):
        	output.write(str(j[k]) + ' ')
		output.write('\n')
    inputf.close()
    output.close()


def flatten_red():

    inputf = open("cake.ppm", "r")
    output = open("cakemodify.ppm", "w+")

    output.write(inputf.readline())
    output.write(inputf.readline())
    output.write(inputf.readline())
    for i in inputf.readlines():
                j = i.split()
            	for k in range(0, len(j), 3):
                	j[k] = 0
			j[k+1] = j[k+1]
			j[k+2] = j[k+2]
            	for k in range(0, len(j), 1):
        		output.write(str(j[k]) + ' ')
        		output.write('\n')
    inputf.close()
    output.close()


def flatten_green():

    inputf = open("cake.ppm", "r")
    output = open("cakemodify.ppm", "w+")

    output.write(inputf.readline())
    output.write(inputf.readline())
    output.write(inputf.readline())
    for i in inputf.readlines():
                j = i.split()
            	for k in range(0, len(j), 3):
			j[k] = j[k]
                	j[k+1] = 0
			j[k+2] = j[k+2]
            	for k in range(0, len(j), 1):
        		output.write(str(j[k]) + ' ')
        		output.write('\n')
    inputf.close()
    output.close()


def flatten_blue():

    inputf = open("cake.ppm", "r")
    output = open("cakemodify.ppm", "w+")

    output.write(inputf.readline())
    output.write(inputf.readline())
    output.write(inputf.readline())
    for i in inputf.readlines():
                j = i.split()
            	for k in range(0, len(j), 3):
			j[k] = j[k]
			j[k+1] = j[k+1]
                	j[k + 2] = 0
            	for k in range(0, len(j), 1):
    			output.write(str(j[k]) + ' ')
        		output.write('\n')
    inputf.close()
    output.close()


def main():
	print ('1.Convert to Greyscale')
	print ('2.Negative of red')
	print ('3.Negative of green')
	print ('4.Negative of Blue')
	print ('5.Flatten red')
	print ('6.Flatten green')
	print ('7.Flatten blue')
	print ('Do you want [1]? (y/n)')
	print('Enter the choice: Type y or n beside each filter ')
	GS = input('Convert to Greyscale[y/n]: ')
	NR = input('Negate Red[y/n]: ')
	NG = input('Negate Green[y/n]: ')
	NB = input('Negate Blue[y/n]: ')
	FR = input('Flatten Red[y/n]: ')
	FG = input('Flatten Green[y/n]: ')
	FB = input('Flatten Blue[y/n]: ')
	if(GS == 'y'):
	        greyscale()
	
	if(NR == 'y'):
	        negatered()
	if(NG == 'y'):
	        negategreen()
	if(NB == 'y'):
	        negateblue()
	if(FR == 'y'):
	        flattenred()
	if(FG == 'y'):
	        flattengreen()
	if(FB == 'y'):
	        flattenblue()

if __name__ == '__main__':
    main()
