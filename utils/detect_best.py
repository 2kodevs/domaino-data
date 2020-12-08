import json

data = json.load(open('data/data.json', 'r'))

strategies = {
    'Normal': {},
    'Supportive': {}
}
strategies55 = {}
counts = {}

for n in data.values():
    for g in n.values():
        for r in g.values():
            for p, dp in r.items():
                for s, ds in dp.items():
                    k = f'{p}-{s}'
                    for v in ds.values():
                        strategies[p][k] = strategies[p].get(k, 0) + v
                        strategies55[k] = strategies55.get(k, True) and v >= 55
                    counts[k] = counts.get(k, 0) + len(ds)

best_by_mean = []
best_55 = []

for p in strategies.keys():
    best = ('', 0)
    for k, s in strategies[p].items():
        mean = strategies[p][k] / counts[k]
        if mean > best[1]:  
            best = (k, mean)   

        if strategies55[k]:
            best_55.append(k)
    
    best_by_mean.append(best)

print('Best by mean:')
print(best_by_mean[0], '-----', best_by_mean[1])

print('Strategies with absolute values greater than 55:')
print(best_55)
