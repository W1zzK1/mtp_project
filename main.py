from pymetro.pymetro import *

w = Router([12])
source, target = Station(13), Station(28)
r = w.make_route(source, target)


print(r)
print(f'Путь {r.path}')
print(f'Время пути в минутах {r.time / 60}')
