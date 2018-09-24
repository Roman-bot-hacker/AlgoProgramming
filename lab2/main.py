from tree import Tree

if __name__ == '__main__':
    #initialize tree
    tree = Tree()

    #read from file
    array = [1, 34, 87, 32, 12, 65, 19, 3, 73, 879, 2, 34, 980, 1222, 25, 31, 865, 8]

    #insert to tree
    for item in array:
        tree.insert(item)

    #find we need

    #print result
    tree.print_result()