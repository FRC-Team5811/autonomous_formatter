print(".BOND Element Transformation Environment Resolver")
print("by Luke and Tom")
print()

while True:
    filename = input("load .BOND file: ")

    infile = filename + ".BOND"
    outfile = filename + ".txt"
    # numcol = int(input("number of columns: "))
    try:
        with open(infile, "r") as f:
            text = f.read()
            lines = text.splitlines()

            cols = [[] for i in range(len(lines[0].split()))]

            for l in lines:
                words = l.split()
                for i, w in enumerate(words):
                    try:
                        cols[i].append(w)
                    except IndexError:
                        cols.append([])
                        cols[i].append(w)

        formatted_list = []

        for n, c in enumerate(cols):
            formatted = ""
            for ni, i in enumerate(c):
                formatted += i
                if ni != len(c) - 1:
                    formatted += ", "
            formatted_list.append(formatted + "\n")

        with open(outfile, "w+") as f:
            f.write("\t\t\tvoltagesRight = new ArrayList(\n\t\t\t\tArrays.asList(" + formatted_list[0] + "\t\t\t\t)\n\t\t\t);\n")
            f.write("\t\t\tvoltagesLeft = new ArrayList(\n\t\t\t\tArrays.asList(" + formatted_list[1] + "\t\t\t\t)\n\t\t\t);\n")
            f.write("\t\t\tposes = new ArrayList(\n\t\t\t\tArrays.asList(" + formatted_list[2] + "\t\t\t\t)\n\t\t\t);\n")
            f.write("\t\t\tvels = new ArrayList(\n\t\t\t\tArrays.asList(" + formatted_list[3] + "\t\t\t\t)\n\t\t\t);\n")
            f.write("\t\t\tangs = new ArrayList(\n\t\t\t\tArrays.asList(" + formatted_list[4] + "\t\t\t\t)\n\t\t\t);\n")
            f.write("\t\t\tangVels = new ArrayList(\n\t\t\t\tArrays.asList(" + formatted_list[5] + "\t\t\t\t)\n\t\t\t);")

            print("done")
    except FileNotFoundError:
        print("invalid file")
