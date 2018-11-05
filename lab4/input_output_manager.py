import csv


class InOutManager:
    graph = dict()

    # read from file with printer's data
    def read_data_from_file(self):
        try:
            with open('references.csv') as csvin:
                reader = csv.reader(csvin)
                row_count = 0
                matrix_size = 0
                for row in reader:
                    if row_count == 0:
                        matrix_size = [int(x) for x in row[0]]
                        row_count += 1
                    else:
                        self.graph[(row_count-1).__str__()] = []
                        for column in range(0, matrix_size[0]):
                            if row[column] == 'y':
                                self.graph[(row_count - 1).__str__()].append(column.__str__())
                        row_count += 1
        except FileNotFoundError:
            print("File with data does not exist!")
        return self.graph

    def write_data_to_file(self, item):
        f = open('answer.txt', "w")
        f.write(item)
        f.close()
