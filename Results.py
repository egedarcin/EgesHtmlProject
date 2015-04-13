scores = {}
result_f = open("results.txt")
for line in result_f:
    (name, score) = line.split()
    scores[score] = name
result_f.close()
print("The Top Scorers Were:")
for each_score in sorted(scores.keys(), reverse = True):
    print('Surfer ' + scores[each_score] + ' scored ' + each_score)
