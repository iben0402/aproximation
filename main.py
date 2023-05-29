import pandas as pd


def calculate_phi(xi):
    n = len(xi)
    wspolczynniki = [0] * (n + 1)
    wspolczynniki[0] = 1

    for i in range(n):
        for j in range(i, -1, -1):
            wspolczynniki[j + 1] -= xi[i] * wspolczynniki[j]

    return wspolczynniki


data = pd.read_csv('./2018_paths/Hel_yeah.csv')
data.columns = ['x','y']
length = len(data)
interpolation_function = []
xi = []
divider = 1

for i in range(length):
    for j in range(length):
        if i!=j:
            xi.append(data['x'][j])
            divider *= (data['x'][i]-data['y'][j])
    divider = divider / data['y'][i]
    phi = calculate_phi(xi)
    phi = [x / divider for x in phi]
    if i == 0:
        interpolation_function = phi
    else:
        for k in range(len(interpolation_function)):
            interpolation_function[k]+=phi[k]

    xi = []
    divider = 1

print(interpolation_function)

# xi = data['x']
# print(calculate_phi(xi))