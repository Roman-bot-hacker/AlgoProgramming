import csv


class InOutManager:
    graph = dict()

    # read from file with printer's data
    @staticmethod
    def read_data_from_file():
        try:
            with open('references.csv') as csvin:
                reader = csv.reader(csvin)
                keys_set = set()
                for row in reader:
                    parent = row[0]
                    if parent in keys_set:
                        child = row[1]
                        InOutManager.graph[parent].append(child)
                    else:
                        keys_set.add(parent)
                        child = [row[1]]
                        InOutManager.graph[parent] = child
        except FileNotFoundError:
            print("File with data does not exist!")

    @staticmethod
    def write_data_to_file(list):
        f = open('answer.txt', "w")
        for item in list:
            f.write(item + "\n")
        f.write("\n")
        f.close()
