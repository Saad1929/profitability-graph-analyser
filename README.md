# Profitability Graph Analyser - Python
## Brief Summary
- Personal Project which employs **Python** to generate **visually intuitive graphs** from stock sales data **retrieved from a database** through **Comma-Separated Values (CSV) file handling**.
- The project is now **fully operational** and being **utilised at a local convenience store**.
- The project was **planned collaboratively** with the **involvement of two other developers**, emphasising **teamwork** in software design and development.
## 🎯Aims and Motivation
- The **primary objective** of this project was to enable users to **effortlessly visualise** their sales data from the database through **graphical representation**, aiding in better **comprehension and analysis**.
- **Motivated** by an **unrelenting passion for knowledge and personal growth**, I took on the **responsibility** of utilising **back-end technologies** to assist others as well as **expanding my expertise in back-end technologies**.
## ⚙️Technologies, Requirements and Software Tools
### Programming & Scriping Languages
- Python3
- MySQL
### Pip & Python Package Requirements
- Matplotlib
### Other Software Tools
- **Comma-Separated Values (CSV)** files were utilised in conjunction with **file handling operations** as part of the project's implementation.
- **Git** was used as a **Version Control System (VCS)** to **maintain a history of the software project**.
- **GitHub** was used to **host and maintain history of the project**.
## ✏️Design
### Back-End Technology Stack
- As a **back-end project**, **Python3** was employed to develop **profitability graphs** using the **matplotlib package** which enables users to **conveniently monitor and track the performance of products**, identifying both **successful and underperforming items**.
- Upon converting database information into a **CSV file**, a **sophisticated data structure** was created which was used to **store the information retrieved from the database** using **CSV File Handling**. In this case, a **dictionary data structure** was implemented, where the month number served as the key, and the corresponding values were arrays that stored the sale numbers per month.
- A function named "filter_by_characteristic" was created, which accepts the data structure and the item by which the user wishes to filter, **facilitating the convenient plotting and viewing of sale data**.
- The function named "aggregate_by_characteristic" achieves a similar result.
- The "plot_total_profit" function takes the data structure as input and generates a **visually appealing line graph that illustrates the months and total profits**. The line graph presents the sales information in a **modern and aesthetically pleasing manner**.
- The "plot_histogram_total_units" function achieves a similar outcome as the "plot_total_profit" function, but instead of a line graph, it generates a **histogram** that showcases the **frequencies and distribution of total units sold**. This graphical representation offers an **alternative visual perspective for analysing sales data**.
- The "plot_toothpaste_sales" function displays the **overall sales of a specific product**, in this case toothpaste, along with the total sales for each month. This function provides a **graphical representation** that **highlights the sales performance of the product over time**.
## 🚀 Graph Screenshots
### Monthly Profit Line Graph
![Monthly_Profit](https://github.com/Saad1929/profitability-graph-analyser/assets/108022733/4876e54c-d194-48e7-b33c-a6edab8f4fa7)
### Frequency Histogram

