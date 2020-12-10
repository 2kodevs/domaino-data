import json

data = json.load(open('data/data.json', 'r'))

strategies = {
    'Normal': {},
    'Supportive': {}
}
strategies55 = {}
counts = {}

for game in data.values():
    for rule in game.values():
        for behavior in rule.values():
            for prefix, d_prefix in behavior.items():
                for strategy, d_strategy in d_prefix.items():
                    k = f'{prefix}-{strategy}'
                    for v in d_strategy.values():
                        strategies[prefix][k] = strategies[prefix].get(k, 0) + v
                        strategies55[k] = strategies55.get(k, True) and v >= 55
                    counts[k] = counts.get(k, 0) + len(d_strategy)

best_by_mean = {
    'Normal':     [],
    'Supportive': []
}
best_55 = []

for p in strategies.keys():
    for k, s in strategies[p].items():
        mean = strategies[p][k] / counts[k]
        best_by_mean[p].append((mean, k))

        if strategies55[k]:
            best_55.append(k)

for v in best_by_mean.values(): 
    v.sort(reverse=True)

print('Best by mean:')
for k, v in best_by_mean.items():
    print(k)
    for s in v[:5]:
        print(s)

print('Strategies with absolute values greater than 55:')
print(best_55)
