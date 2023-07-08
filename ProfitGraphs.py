import matplotlib.pyplot as plt
plt.style.use("seaborn")

try:
    f = open("company-sales.csv", "r")
except FileNotFoundError:
    print("The CSV File cannot be found. Please ensure the file is in the same directory as the file 'ProfitGraphs.py'.")

def read_data(filename):
    company_sales_data = {}

    line = filename.readline()[:-1]
    while line != "":
        list_line = line.split(sep=",")
        assert len(list_line) == 9, "There is a line in the file which doesn't contain the correct sales data!"
        try: 
            first_line = int(list_line[0])
            if type(first_line) == type(1):
                for item in list_line:
                    month_number = list_line[0]
                    company_sales_data[int(month_number)] = [float(value) for value in list_line[1:]]