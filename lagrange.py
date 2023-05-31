from data import get_data_random, get_data_regular, get_all_data
import numpy as np
import matplotlib.pyplot as plt


def lagrange_interpolation(x, y, xi):
    n = len(x)
    yi = 0.0
    for i in range(n):
        L = 1.0
        for j in range(n):
            if i != j:
                L *= (xi - x[j]) / (x[i] - x[j])
        yi += y[i] * L
    return yi

def interpolate_with_lagrange(name_of_file, amount_of_points, way_of_choosing_data='regular'):
    file_path = './2018_paths/' + name_of_file + '.csv'
    if way_of_choosing_data == 'regular':
        x, y = get_data_regular(file_path, amount_of_points)
    elif way_of_choosing_data == 'random':
        x, y = get_data_random(file_path, amount_of_points)
    else:
        print("Wrong way of choosing data")
        return

    # Interpolacja dla nowych punktów
    xi = np.linspace(x[0], x[-1], 1000)  # Nowe punkty x dla aproksymacji
    yi = np.array([lagrange_interpolation(x, y, xi_val) for xi_val in xi])  # Interpolowane wartości y

    # Wyświetlanie wyników
    all_x, all_y = get_all_data(file_path)

    plt.figure(figsize=(10, 6))
    plt.plot(all_x, all_y, 'g-', label='Wszystkie dane')
    plt.plot(x, y, 'bo', label='Dane wejściowe (węzły)')
    plt.plot(xi, yi, 'r-', label='Interpolacja Lagrange\'a')
    plt.xlabel('Odległość')
    plt.ylabel('Wysokość')
    plt.title('Aproksymacja profilu wysokościowego\n pliku ' + name_of_file + '.csv metodą Lagrange\'a' + ' dla ' + str(amount_of_points) + ' punktów. Punkty dobierane: ' + way_of_choosing_data + '.')
    plt.legend()
    plt.grid(True)

    # Ustawianie zakresu osi y
    y_min = np.min(y)*0.7
    y_max = np.max(y)*1.3
    plt.ylim(y_min, y_max)

    # Wyświetlanie wykresu
    #plt.show()

    # Zapisywanie wykresu
    plot_filename = "./plots/" + name_of_file + "_" + way_of_choosing_data + "_" + str(amount_of_points) + "_lagrange.png"
    plt.savefig(plot_filename)
    plt.close()


