scores = []
names = []
result_f = open("results.txt")
for line in result_f:
    (name, score) = line.split()
    scores.append(float(score))
    names.append(name)
result_f.close()
scores.sort(reverse = True)
names.sort (reverse = True)
print("The Top Scorers Were:")
print(names[0] + ' scored ' + str(scores[0]))
print(names[1] + ' scored ' + str(scores[1]))
print(names[2] + ' scored ' + str(scores[2]))
