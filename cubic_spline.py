from data import get_data_regular, get_data_random, get_all_data
import numpy as np
import matplotlib.pyplot as plt


def cubic_spline(x, y, filename, way_of_choosing_data):
    n = len(x) - 1  # n - ilość podprzedziałów
    h = np.diff(x)  # różnice między kolejnymi węzłami - hi

    A = np.zeros((4 * n, 4 * n))
    B = np.zeros(4 * n)

    # Wypełnianie macierzy A i wektora B
    for i in range(n):
        # krok 1: aj = yj
        A[i, 4 * i] = 1
        B[i] = y[i]
        # krok 2: aj + bj*hj + cj*hj^2 + dj*hj^3 = yj+1
        A[n + i, 4 * i] = 1
        A[n + i, 4 * i + 1] = h[i]
        A[n + i, 4 * i + 2] = h[i] ** 2
        A[n + i, 4 * i + 3] = h[i] ** 3
        B[n + i] = y[i + 1]
        # krok 3: bj-1 + 2*cj-1*hj-1 + 3*dj-1*hj-1^2 = bj (dla j =1, 2, ..., n-1)
        if i > 0:
            A[(2 * n) + i - 1, 4 * (i - 1) + 1] = 1
            A[(2 * n) + i - 1, 4 * (i - 1) + 2] = 2 * h[i - 1]
            A[(2 * n) + i - 1, 4 * (i - 1) + 3] = 3 * h[i - 1] ** 2
            A[(2 * n) + i - 1, 4 * i + 1] = -1
        # krok 4: - 2cj + 2cj-1 +6dj-1*hj-1 = 0 (dla j =1, 2, ..., n-1)
        if i > 0:
            A[3 * n + i - 2, 4 * (i - 1) + 2] = 2
            A[3 * n + i - 2, 4 * i + 2] = -2
            A[3 * n + i - 2, 4 * (i - 1) + 3] = 6 * h[i - 1]
        # krok 5: c0 = 0
        if i == 0:
            A[-2, 2] = 1
        # krok 6: 2cn-1 + 6dn-1*hn-1 = 0
        if i == n - 1:
            A[-1, 4 * (n - 1) + 2] = 2
            A[-1, 4 * (n - 1) + 3] = 6 * h[n - 1]

    # Rozwiązanie układu równań
    M = np.linalg.solve(A, B)
    # Współczynniki wielomianów. Zakomentuj jeśli nie będzie już potrzebne
    # print("Wspolczynniki wielomianow: ")
    # print(M)

    # Interpolacja dla nowych punktów
    xi = np.linspace(x[0], x[-1], max(1000, 100*n))
    yi = np.zeros_like(xi)

    for i in range(n):
        mask = (xi >= x[i]) & (xi <= x[i + 1])
        dx = xi[mask] - x[i]
        dy = M[4 * i] + M[4 * i + 1] * dx + M[4 * i + 2] * dx ** 2 + M[4 * i + 3] * dx ** 3
        yi[mask] = dy

    filepath = "./2018_paths/" + filename + ".csv"
    all_x, all_y = get_all_data(filepath)

    # Wykres
    plt.figure(figsize=(10, 6))
    plt.plot(all_x, all_y, 'g-', label='Wszystkie dane')
    plt.plot(x, y, 'bo', label='Dane wejściowe (węzły)')
    plt.plot(xi, yi, 'r-', label='Funkcje sklejane')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolacja funkcją sklejaną dla ' + str(n) + ' podprzedziałów \n Dla pliku: ' + filename + ' i sposobu wyboru danych: ' + way_of_choosing_data)
    plt.legend()
    plt.grid(True)

    # Wyświetlenie wykresu
    #plt.show()

    # Zapis do pliku
    plot_filename = "./plots/" + filename + "_" + way_of_choosing_data + "_" + str(n+1) + "_cubic_spline.png"
    plt.savefig(plot_filename)
    plt.close()

def interpolate_with_cubic_splines(filename, amount_of_points, way_of_choosing_data='regular'):
    filepath = "./2018_paths/" + filename + ".csv"
    if way_of_choosing_data == 'regular':
        x, y = get_data_regular(filepath, amount_of_points)
    elif way_of_choosing_data == 'random':
        x, y = get_data_random(filepath, amount_of_points)
    else:
        print("Wrong way of choosing data!")
        return
    cubic_spline(x, y, filename, way_of_choosing_data)