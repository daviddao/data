import matplotlib.pyplot as plt

scores_500 = []

f = open("../worst-case-dataset/500_iterations/RAxML_RF-Distances.T499")

for line in f:
    line = line.split()
    scores_500.append(float(line[1]))

f.close()

n, bins, patches = plt.hist(scores_500, 50, normed=0, facecolor='b', alpha=0.75)
plt.xlabel('RF distance')
plt.ylabel('# of trees')
plt.title('Histogram of RF distances (500 Iterations)')
plt.show()
