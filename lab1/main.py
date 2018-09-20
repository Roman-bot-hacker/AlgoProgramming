from printer import Printer
from counter import Counter
from datetime import datetime
from selection_sort import selection_sort
from quicksort import Quicksort
import csv


#read from file with printer's data
def read_data_from_file():
    printer_list = []
    try:
        with open('printer_data.csv') as csvin:
            reader = csv.reader(csvin)
            for row in reader:
                new_printer = Printer(row[0], int(row[1]), int(row[2]))
                printer_list.append(new_printer)
    except FileNotFoundError:
        print("File with data does not exist!")
    return printer_list


#find out time of algorithm's work
def work_time(start, finish) :
    return finish - start


#func to print sorting result
def print_answer(algo_name, work_time, compare_num, exchange_num, sorted_list):
    print(str(algo_name)+"\nWORK TIME: "+str(work_time)+"\nCOMPARISON NUMBER: "+str(compare_num)+
          "\nEXCHANGE NUMBER: "+str(exchange_num)+"\nSORT RESULT: \n"+str(sorted_list))


#main method
if __name__ == "__main__":

    printer_list = read_data_from_file()
    start = datetime.now().microsecond
    select_sorted_list = selection_sort(printer_list)
    finish = datetime.now().microsecond
    print_answer("SELECTION SORT", work_time(start, finish), Counter.compare_num,
                 Counter.exchange_num, select_sorted_list)
    print("\n\n-------------------------------------------------------------------------------------------\n\n")
    Counter.count_reset()
    quicksort = Quicksort(printer_list)
    start = datetime.now().microsecond
    quicksort.quick_sort(0, len(printer_list)-1)
    finish = datetime.now().microsecond
    print_answer("QUICKSRT", work_time(start, finish), Counter.compare_num, Counter.exchange_num, quicksort.sort_list)
    print("\n\n-------------------------------------------------------------------------------------------\n\n")
