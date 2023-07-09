import matplotlib.pyplot as plt
plt.style.use("seaborn")

def read_file(filename):
    try:
        f = open("company-sales.csv", "r")
        return f
    except FileNotFoundError:
        print("The CSV File cannot be found. Please ensure the file is in the same directory as the file 'ProfitGraphs.py'.")

#Reads CSV File and Returns a Dictionary Data Structure to further work with data.
def read_data(filename):
    f = read_file(filename)
    company_sales_data = {}

    line = f.readline()[:-1]
    while line != "":
        list_line = line.split(sep=",")
        assert len(list_line) == 9, "There is a line in the file which doesn't contain the correct sales data!"
        try:
            first_line = int(list_line[0])
            if type(first_line) == type(1):
                for item in list_line:
                    month_number = list_line[0]
                    company_sales_data[int(month_number)] = [float(value) for value in list_line[1:]]
        except (TypeError, FileNotFoundError, AssertionError, ValueError):
            if TypeError:
              pass
            elif FileNotFoundError:
                print("The file you entered does not seem to exist. Please Try Again.\n")
            elif AssertionError:
                print("There is a line in the file which doesn't contain the correct sales data!")
            elif ValueError:
                pass
        line = f.readline()[:-1]
    return company_sales_data

data = read_data("company-sales.csv")

#This function is designed to accept a product and filter the main dictionary to display the relevant data for that specific product.
def filter_by_characteristic(dictionary, characteristic):
    items_in_csv = {"FACECREAM": 0,
                    "FACEWASH": 1,
                    "TOOTHPASTE": 2,
                    "BATHING SOAP": 3,
                    "SHAMPOO": 4,
                    "MOISTURISER": 5,
                    "TOTAL UNITS": 6,
                    "TOTAL PROFIT": 7}
    filtered_items = {}
    try:
        month = 1
        filter_characteristic = items_in_csv[ characteristic.upper()]
        for key, value in dictionary.items():
            assert key not in filtered_items.keys(), "Month already exists in the dictionary."
            assert month <= 12, "Invalid month number"
            filtered_items[month] = value[filter_characteristic]
            month += 1
        return filtered_items
    except (KeyError, ValueError):
        print("The item that you entered does not exist. Please take a look below at the options & try again.\n")
        for key in items_in_csv.keys():
            print(key.title())
        print("\n", end= "")

#Function is used to select any column from the database and calculate the average value for that column.
def aggregate_by_characteristic(dictionary, characteristic):
    items_in_csv = {"FACECREAM": 0,
                    "FACEWASH": 1,
                    "TOOTHPASTE": 2,
                    "BATHING SOAP": 3,
                    "SHAMPOO": 4,
                    "MOISTURIZER": 5,
                    "TOTAL UNITS": 6,
                    "TOTAL PROFIT": 7}
    filtered_items = {}
    total_price = 0
    month = 1
    try:
        filter_characteristic = items_in_csv[characteristic.upper()]
        for key, value in dictionary.items():
            assert key not in filtered_items.keys(), "Month already exists in the dictionary."
            assert month <= 12, "Invalid month number"
            filtered_items[month] = value[filter_characteristic]
            month += 1
        for filtered_value in filtered_items.values():
            total_price += filtered_value
        mean_price = total_price / len([month_number for month_number in filtered_items.keys()])
        return mean_price
    except (KeyError, ValueError):
        print("The item that you entered does not exist. Please take a look below at the options & try again.\n")
        for key in items_in_csv.keys():
            print(key.title())
        print("\n", end="")