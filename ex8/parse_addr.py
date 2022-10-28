# INPUT
# S 0x7ff0008e8,1
# I  0x400590,4
# L  0x601020,6
# I  0x400596,8
# S 0x7ff0008e0,2
# M  0x4fdf720,6
import sys
def parse(fName):
    instructions = []
    insNum = 0
    dataNum = 0
    {("I", "0x400") : 2}
    pgCount = {}
    data2 = []
    f = open(fName, "r")
    for line in f:
        data = line.strip().split(",")[0].split()
        ins = data[0].strip()
        addr = data[1].strip()
        pg = int(addr, 16) // 4096
        
        if ins == "I":
            pgCount[(ins, pg)] = pgCount.get((ins, pg), 0) + 1
            # instructions.append(pg + ',' + pgCount[pg])
        else:
            pgCount[(ins, pg)] = pgCount.get((ins, pg), 0) + 1
            #data.append(pg + ',' + pgCount[pg])

    for key in pgCount:
        if key[0] == "I":
            instructions.append(hex(key[1]) + ',' + str(pgCount[(key[0],key[1])]))
            insNum += pgCount[key[0], key[1]]
        else:
            data2.append(hex(key[1]) + ',' + str(pgCount[(key[0],key[1])]))
            dataNum += pgCount[key[0], key[1]]
    
 
    print("Instructions")
    for line in instructions:
        print(line)
    
    print("Data")
    for line in data2:
        print(line)
        
        
    print("TOTAL INS: ", insNum)
    print("TOTAL DATA: ", dataNum)

            

    

    return None 

parse(sys.argv[1])