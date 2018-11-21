import fileinput
num = 0
metrics = {}
with open("metrics.log", 'r') as f:
    for line in f:
        fields = line.split("\t")
        metric = fields[1]
        metrics[metric] = fields[3] if 3 < len(fields) else ""
for k in sorted(metrics):
    print(k, metrics[k], sep="\t")
