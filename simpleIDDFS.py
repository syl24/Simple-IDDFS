## Small CSP solver using IDDFS
## When given initial domains and constraints
## Main function has input of list of nodes and
## IDDFS will output visited nodes with solution domains
## and number of constraint checks, CNS
## The Main function checks iteratively, and Constraint
## Checker will be called each time

## Initial domain values
list = {
    "A": [1,2,3,4],
    "B": [1,2,3,4],
    "C": [1,2,3,4],
    "D": [1,2,3,4],
    "E": [1,2,3,4],
    "F": [1,2,3,4],
    "G": [1,2,3,4],
    "H": [1,2,3,4]
}

## Counter for how many contraint checks are done
CNS = 0

## Visited node list
visited = {}

## Constraint checker, everytime the Main adds a new node,
## ConstraintChecker is called, and automatically prunes any domain value that
## violates constraints. IDDFS is used.
    
def ConstraintChecker (visited):

    global CNS

    # A >= G
    if "G" in visited:
            ag = 0
            for i in visited["A"]:
                for j in visited["G"]:

                    CNS+= 1
                    if not (i >= j):
                        print(f' A=" {i} G= {j} failure')
                        ag += 1
                        if ag == len(visited["G"]) and i in visited["A"]:
                            visited["A"].remove(i)

    # A < H
    if "H" in visited:
            ah = 0
            for i in visited["A"]:
                for j in visited["H"]:
                    CNS+= 1
                    if not (i < j):
                        print(f' A= {i} H= {j} failure')
                        ah += 1
                        if ah == len(visited["G"]) and i in visited["A"]:
                            visited["A"].remove(i)
            
    # G < H
    if "H" in visited:
            gh = 0
            for i in visited["G"]:
                for j in visited["H"]:
                    CNS += 1
                    if not (i < j):
                        print(f'G= {i} H= {j} failure')
                        gh += 1
                        if gh == len(visited["H"]) and i in visited["G"]:
                            visited["G"].remove(i)

    # H != D
    if "H" in visited:
            hd = 0
            for i in visited["D"]:
                for j in visited["H"]:
                    CNS += 1
                    if not (i != j):
                        print(f'D= {i} H= {j} failure')
                        hd += 1
                        if hd == len(visited["H"]) and i in visited["D"]:
                            visited["D"].remove(i)

    # D >= G
    if "G" in visited:
            dg = 0
            for i in visited["D"]:
                for j in visited["G"]:
                    CNS += 1
                    if not (i >= j):
                        print(f'D= {i} G= {j} failure')
                        dg += 1
                        if dg == len(visited["G"]) and i in visited["D"]:
                            visited["D"].remove(i)
    
    # D != C
    if "D" in visited:
            cd = 0
            for i in visited["C"]:
                for j in visited["D"]:
                    CNS += 1
                    if not (i != j):
                        print(f' C= {i} D= {j} failure')
                        cd += 1
                        if cd == len(visited["D"]) and i in visited["C"]:
                            visited["C"].remove(i)
            
    # E != C
    if "E" in visited:
            ce = 0
            for i in visited["C"]:
                for j in visited["E"]:
                    CNS += 1
                    if not (i != j):
                        print(f' C= {i} E= {j} failure')
                        ce += 1
                        if ce == len(visited["E"]) and i in visited["C"]:
                            visited["C"].remove(i)
            
    # E < D - 1
    if "E" in visited:
            de = 0
            for i in visited["D"]:
                for j in visited["E"]:
                    CNS += 1
                    if not ((i-1) > j):
                        print(f'C= {i} D= {j} failure')
                        cd += 1
                        if cd == len(visited["D"]) and i in visited["C"]:
                            visited["C"].remove(i)
            
    # E != H - 2
    if "H" in visited:
            eh = 0
            for i in visited["H"]:
                for j in visited["E"]:
                    CNS += 1
                    if not (i != (j-2)):
                        print(f'E= {i} H= {j} failure')
                        eh += 1
                        if cd == len(visited["H"]) and i in visited["E"]:
                            visited["E"].remove(i)

    # G != F
    if "G" in visited:
            fg = 0
            for i in visited["F"]:
                for j in visited["G"]:
                    CNS += 1
                    if not (i != j):
                        print(f'F= {i} G= {j} failure')
                        fg += 1
                        if fg == len(visited["G"]) and i in visited["F"]:
                            visited["F"].remove(i)

    # H != F
    if "H" in visited:
            fh = 0
            for i in visited["F"]:
                for j in visited["H"]:
                    CNS += 1
                    if not (i != j):
                        print(f'F= {i} H= {j} failure')
                        fh += 1
                        if fh == len(visited["H"]) and i in visited["F"]:
                            visited["F"].remove(i)

    # C != F
    if "F" in visited:
            cf = 0
            for i in visited["C"]:
                for j in visited["F"]:
                    CNS += 1
                    if not (i != j):
                        print(f' C= {i} F= {j} failure')
                        cf += 1
                        if cf == len(visited["F"]) and i in visited["C"]:
                            visited["C"].remove(i)

    # D != F
    if "F" in visited:
            df = 0
            for i in visited["D"]:
                for j in visited["F"]:
                    CNS += 1
                    if not (i != j):
                        print(f'D= {i} F= {j} failure')
                        df += 1
                        if df == len(visited["F"]) and i in visited["D"]:
                            visited["D"].remove(i)

    # |F-B| = 1
    if "F" in visited:
            bf = 0
            for i in visited["B"]:
                for j in visited["F"]:
                    CNS += 1
                    if not (abs(j - i) == 1):
                        print(f'B= {i} F= {j} failure')
                        bf += 1
                        if bf == len(visited["F"]) and i in visited["B"]:
                            visited["B"].remove(i)

    # |F-B| = 1
    if "F" in visited:
            bf = 0
            for i in visited["B"]:
                for j in visited["F"]:
                    CNS += 1
                    if not (abs(j - i) == 1):
                        print(f'B= {i} F= {j} failure')
                        bf += 1
                        if bf == len(visited["F"]) and i in visited["B"]:
                            visited["B"].remove(i)

    # |G - C| = 1
    if "G" in visited:
            cg = 0
            for i in visited["C"]:
                for j in visited["G"]:
                    CNS += 1
                    if not (abs(j - i) == 1):
                        print(f'C= {i} G= {j} failure')
                        cg += 1
                        if cg == len(visited["G"]) and i in visited["C"]:
                            visited["C"].remove(i)

    # |H-C| is even
    if "H" in visited:
            ch = 0
            for i in visited["C"]:
                for j in visited["H"]:
                    CNS += 1
                    if not ((abs(j - i) % 2) == 0):
                        print(f'B= {i} F= {j} failure')
                        bf += 1
                        if bf == len(visited["F"]) and i in visited["B"]:
                            visited["B"].remove(i)

    # |E-F| is odd
    if "F" in visited:
            ef = 0
            for i in visited["E"]:
                for j in visited["F"]:
                    CNS += 1
                    if not ((abs(i - j) % 2) == 1):
                        print(f' E= {i} F= {j} failure')
                        ef += 1
                        if ef == len(visited["F"]) and i in visited["E"]:
                            visited["E"].remove(i)
    
    return visited


## Helper function to print results

def printHelper(visited):
    global CNS
    result = ""
    for x in visited:
          print(x, visited)
          result = str(x) + " = " + str(visited[x])
    print(f'{result}')
    print(f' Number of contraint checks {CNS}')


## Main function for IDDFS CSP solver
## Notice the ConstraitChecker will auto prune and
## has DFS built in. Main function feeds nodes
## one by one

def main():
    while len(list) > len(visited):
        for x in list.keys():
            visited[x] = list[x]
            ConstraintChecker(visited)
    printHelper(visited)
    
main()
