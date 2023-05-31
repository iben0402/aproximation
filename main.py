from lagrange import interpolate_with_lagrange
from cubic_spline import interpolate_with_cubic_splines

# UWAGA: Obecnie wszystkie wykresy zapisywane są do plików, a nie wyświetlane na ekranie.
# PLIK 100.csv
interpolate_with_lagrange('100', 10, 'regular')
interpolate_with_lagrange('100', 10, 'random')
interpolate_with_lagrange('100', 20, 'regular')
interpolate_with_lagrange('100', 20, 'random')

interpolate_with_cubic_splines('100', 20, 'regular')
interpolate_with_cubic_splines('100', 20, 'random')
interpolate_with_cubic_splines('100', 50, 'regular')
interpolate_with_cubic_splines('100', 50, 'random')

# PLIK MountEverest.csv
interpolate_with_lagrange('MountEverest', 10, 'regular')
interpolate_with_lagrange('MountEverest', 10, 'random')
interpolate_with_lagrange('MountEverest', 20, 'regular')
interpolate_with_lagrange('MountEverest', 20, 'random')

interpolate_with_cubic_splines('MountEverest', 20, 'regular')
interpolate_with_cubic_splines('MountEverest', 20, 'random')
interpolate_with_cubic_splines('MountEverest', 50, 'regular')
interpolate_with_cubic_splines('MountEverest', 50, 'random')

# PLIK WielkiKanionKolorado.csv
interpolate_with_lagrange('WielkiKanionKolorado', 10, 'regular')
interpolate_with_lagrange('WielkiKanionKolorado', 10, 'random')
interpolate_with_lagrange('WielkiKanionKolorado', 20, 'regular')
interpolate_with_lagrange('WielkiKanionKolorado', 20, 'random')

interpolate_with_cubic_splines('WielkiKanionKolorado', 20, 'regular')
interpolate_with_cubic_splines('WielkiKanionKolorado', 20, 'random')
interpolate_with_cubic_splines('WielkiKanionKolorado', 50, 'regular')
interpolate_with_cubic_splines('WielkiKanionKolorado', 50, 'random')

# PLIK SpacerniakGdansk.csv
interpolate_with_lagrange('SpacerniakGdansk', 10, 'regular')
interpolate_with_lagrange('SpacerniakGdansk', 10, 'random')
interpolate_with_lagrange('SpacerniakGdansk', 20, 'regular')
interpolate_with_lagrange('SpacerniakGdansk', 20, 'random')

interpolate_with_cubic_splines('SpacerniakGdansk', 20, 'regular')
interpolate_with_cubic_splines('SpacerniakGdansk', 20, 'random')
interpolate_with_cubic_splines('SpacerniakGdansk', 50, 'regular')
interpolate_with_cubic_splines('SpacerniakGdansk', 50, 'random')

# PLIK 100.csv dla dużego zestawu danych i metody Lagrange'a
interpolate_with_lagrange('100', 50, 'regular')

