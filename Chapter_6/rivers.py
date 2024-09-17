rivers = {
        'egypt':'nile',
        'italy':'tiber',
        'china':'yangtze',
    }

for k, v in rivers.items():
    print(f'the river {v.title()} runs through {k.title()}.')

for k in rivers:
    print(k.title())

for v in rivers.values():
    print(v.title())