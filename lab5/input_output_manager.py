import csv


class InOutManager:
    distance = 0
    max_heights = []

    # read from file with printer's data
    def read_data_from_file(self):
        try:
            with open('electro_data.csv') as csvin:
                reader = csv.reader(csvin)
                rows_counter = 0
                for row in reader:
                    if rows_counter == 0:
                        self.distance = int(row[0])
                        rows_counter = 1
                    else:
                        for item in row:
                            self.max_heights.append(int(item))
        except FileNotFoundError:
            print("File with data does not exist!")

    def write_data_to_file(self, item):
        f = open('answer.txt', "w")
        f.write(str(item))
        f.close()
