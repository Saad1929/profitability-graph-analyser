import matplotlib.pyplot as plt
plt.style.use("seaborn")

f = open("company-sales.csv", "r")

def read_data_from_csv(filename):
    company_sales_data = {}

    line = filename.readline()[:-1]
    while line != "":
        list_line = line.split(sep=",")
        assert len(list_line) == 9, "There is a line in the file which doesn't contain the correct sales data!"