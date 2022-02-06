import re
#
from optimizer import Optimizer

if __name__ == '__main__':
    count = 0
    c = ':'
    comment = "#"

    branches = ["beq", "beqz", "bge", "bgt", "ble", "blt", "Goto"]

    optimizer = Optimizer()


    with open("test.txt") as fp:
        for line in fp:
            if comment in line:
                continue
            if c in line:
                # print(line.strip()[0:-1])
                # print(optimizer.scopes)
                optimizer.new_scope(name=line.strip()[0:-1])




    with open("test.txt") as fp:
        current_scope = "root"
        for line in fp:

            if comment in line:
                continue
            if c in line:
                current_scope = line.strip()[0:-1]
            for branch_name in branches:
                if len(line.strip()) > 0 and  re.search(r'\b' + branch_name + r'\b', line.strip()):
                    print(line , "ccc")
                    print(branch_name)
                    new_branch = line.split(",")[-1].strip()
                    print(new_branch)
                    print("------")
                    child_scope = optimizer.get_scope(new_branch)
                    parent_scope = optimizer.get_scope(current_scope)
                    child_scope.add_parent(parent_scope)