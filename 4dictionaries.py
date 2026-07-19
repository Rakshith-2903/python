meanings={
            'bat':'used to hit',
            'ball':'to be hit',
            'wicket':'to be protected'
        }
print(meanings)
print(meanings['bat'])
meanings['gloves']='used to catch'
print(meanings)
meanings.pop('wicket')
print(meanings)