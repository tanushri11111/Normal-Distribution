import plotly.figure_factory as ff
import pandas as pd
import statistics
import csv

df = pd.read_csv("StudentsPerformance.csv") 

findList= df["reading score"].tolist()
mean = statistics.mean(findList)
print("Mean is:-")
print(mean)
median = statistics.median(findList)
print("Median is :-")
print(median)
mode = statistics.mode(findList)
print("Mode is :-")
print(mode)

standardDeviation=statistics.stdev(findList)
print("Standard Deviation is :-")
print(format(standardDeviation))

first_std_deviation_start, first_std_deviation_end = mean-standardDeviation, mean+standardDeviation
second_std_deviation_start, second_std_deviation_end = mean-(2*standardDeviation), mean+(2*standardDeviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*standardDeviation), mean+(3*standardDeviation)

list_of_data_within_1_std_deviation=[result for result in findList if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation=[result for result in findList if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation=[result for result in findList if result > third_std_deviation_start and result < third_std_deviation_end]
print("{}% of data lies within first standard deviation".format(len(list_of_data_within_1_std_deviation)*100/len(findList)))
print("{}% of data lies within second standard deviation".format(len(list_of_data_within_2_std_deviation)*100/len(findList)))
print("{}% of data lies within third standard deviation".format(len(list_of_data_within_3_std_deviation)*100/len(findList)))
