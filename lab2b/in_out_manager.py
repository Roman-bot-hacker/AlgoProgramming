import csv
from hamster import Hamster

class InOutManager:

    array = []
    stock = 0
    number = 0

    # read from file with printer's data
    @staticmethod
    def read_data_from_file():
        try:
            with open('hamsters.csv') as csvin:
                reader = csv.reader(csvin)
                i = 0
                for row in reader:
                    if i == 0:
                        InOutManager.stock = int(row[0])
                    elif i == 1:
                        InOutManager.number = int(row[0])
                    else:
                        hamster = Hamster(int(row[0]), int(row[1]))
                        InOutManager.array.append(hamster)
                    i += 1
        except FileNotFoundError:
            print("File with data does not exist!")
