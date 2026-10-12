# #---------Statistics--------

# # Statistics practical implementation
# # Measure of Central Tendency
# # Mean, Median, Mode

# # import numpy as np
# # import statistics as stats
# # import seaborn as sns
# # import matplotlib.pyplot as plt

# # ages = [22, 23, 24, 25, 26, 27, 28, 29, 30]

# # # Mean Median Mode
# # print("Mean:", np.mean(ages))
# # print("Median:", np.median(ages))
# # print("Mode:", stats.mode(ages))

# # # Boxplot
# # sns.boxplot(x=ages)

# # # Show graph
# # plt.show()
# # # Boxplot
# # sns.boxplot(x=ages)
# # plt.show()

# #---------------------- 5 number summary ----------------------

# # import numpy as np

# # ages = [22, 23, 24, 25, 26, 27, 28, 29, 30]
# # q1 , q2 , q3 = np.percentile(ages, [25, 50, 75])
# # print("Q1:", q1)
# # print("Q2:", q2)
# # print("Q3:", q3)

# # # To check outlier [Lower Fence - Higher Fence]
# # iqr = q3 - q1
# # lower_fence = q1 - 1.5 * iqr
# # higher_fence = q3 + 1.5 * iqr
# # print("Lower Fence:", lower_fence)
# # print("Higher Fence:", higher_fence)

# #-------------------Measure of Dispersion-------------------
# #--- 1. Variance 
# #--- 2. Standard Deviation 

# import numpy as np
# import statistics as stats

# ages = [22, 23, 24, 25, 26, 27, 28, 29, 30]
# # print(stats.variance(ages))
# # print(np.var(ages, axis = 0))

# def variance(data, dof = 1):
#     n = len(ages)
#     mean = sum (data) /(n-1)
#     deviations = [(x - mean) ** 2 for x in data]
#     variance = sum(deviations) / (n - 1)
#     return variance

# print(variance(ages))

#----------------------------------------------------------------------------

#-------------------Histogram and PDF--------------------------

# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt

# ages = [20, 23, 45, 65, 34, 43, 67, 34, 12, 76, 34, 56]
# sns.histplot(ages, kde = True)
# plt.show()



















