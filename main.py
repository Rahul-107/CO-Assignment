





FILE_NAME='inputfile.txt'
program = []
bin_program =[]
MAX_LOCATION_COUNTER = 225;
location_counter = [];
iscorret = True;
errors = [];

def remove_Comments(Line):
    flag = False;
    x = 0;
    for x in range(len(Line)):
        if("//" in Line[x]):
            flag = True;
            break

    if(flag):
        index = Line[x].find('//')
        if(index == 0):
            Line = Line[:x]
        else:
            Line = Line[:x+1]
            Line = Line[x][:index]
    return Line

def main():
    for i in program:
        instruction = ""
        Opcode_info,error = Opcode_Table.CheckOpcode(i[0])
        opcode , MRI ,operands , definative ,accept_variable = Opcode_info
        if(MRI == 0):
            instruction = opcode + "00000000"
        else:
            symbol_address = Symbol_Table.getlocation(i[1])
            symbol_address = bin(symbol_address)[2:]
            symbol_address = "0"*(len(symbol_address))+symbol_address
            instruction = opcode + symbol_address
        bin_program.append(instruction)
        location_counter += 1

def main():
    global FILE_NAME
    try:
        f = open(FILE_NAME+"_Output.txt", 'r+')
        f.truncate(0)
    except Exception:
        f = open(FILE_NAME+"_Output.txt", 'w')
        f.close()

def createBinary():
    global bin_program
    global FILE_NAME
    f = open(FILE_NAME+"_Output.txt", 'w')
    for i in program:
        f.write(i)
        f.write("\r\n")
    f.close()
    



if __name__ == "__main__":
    main()