import json

data = json.load(open('table.json', 'r'))
keys = list(data.keys())

second_level = [data[k].keys() for k in keys]
for l in second_level:
    assert l == second_level[0]

table = '<div style="display: flex; justify-content: center;">\n<table class="styled-table">\n'
table += f'<thead>\n<tr>\n<th>Estrategias</th>\n'
for k in keys:
    table += f'<th>{k}</th>\n'
table += '</tr>\n</thead>\n<tbody>\n'
for sk in second_level[0]:
    table += f'<tr>\n<th>{sk}</th>\n'
    for k in keys:
        table += f'<td>{data[k][sk]} %</td>\n'
    table += '</tr>'
table += '</tbody>\n</table>\n</div>\n'
open('table.html', 'w').write(table)
