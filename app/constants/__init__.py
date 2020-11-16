import importlib


__all__ = [
    'common',
    'messages',
]

prefix = 'app.constants'

for i in __all__:
    importlib.import_module(f'{prefix}.{i}')
