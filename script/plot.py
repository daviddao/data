import numpy as np
import matplotlib.pyplot as plt

## Plot for rf scores

f = open("../random_sampling_dataset/250_iterations/rf_scores.txt")

scores_random_250 = []

for line in f:
    line = line.split()
    scores_random_250.append(float(line[0]))

f.close()

scores_250 = []

f = open("../worst-case-dataset/250_iterations/rf_scores.txt")

for line in f:
    line = line.split()
    scores_250.append(float(line[0]))

f.close()


plt.plot(scores_250,'bo',scores_random_250,'g^')
plt.title("Average RF distance vs. Iterations")
plt.xlabel("Average RF distance")
plt.ylabel("Iterations")
plt.show()

## Plot for tree decrease

# f = open("../random_sampling_dataset/250_iterations/rf_scores.txt")

# scores_random_250 = []

# for line in f:
#     line = line.split()
#     scores_random_250.append(float(line[2]))

# f.close()

# scores_250 = []

# f = open("../worst-case-dataset/250_iterations/rf_scores.txt")

# for line in f:
#     line = line.split()
#     scores_250.append(float(line[2]))

# f.close()


# plt.plot(scores_250,'bo',scores_random_250,'g^')
# plt.title("# Trees Analyzed vs. Iterations")
# plt.xlabel("Number of Trees Analyzed")
# plt.ylabel("Iterations")
# plt.show()

## Plot for top scores

# f = open("../random_sampling_dataset/250_iterations/taxa.txt")

# scores_random_250 = []

# for line in f:
#     line = line.split(",")
#     scores_random_250.append(float(line[0]))

# f.close()

# scores_250 = []

# f = open("../worst-case-dataset/250_iterations/taxa.txt")

# for line in f:
#     line = line.split(",")
#     scores_250.append(float(line[0]))

# f.close()

# plt.plot(scores_250,'bo',scores_random_250,'g^')
# plt.title("Top Scores vs. Iterations")
# plt.xlabel("Dropset Score")
# plt.ylabel("Iterations")
# plt.show()

