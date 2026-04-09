import time
import random
import matplotlib.pyplot as plt
import seaborn as sns

# Algoritmo fuerza bruta O(n^2)
# Algoritmo divide y vencerás O(n log n)

# Prueba con arreglo de ejemplo
SIZES = [10, 50, 100, 200, 500, 1000]
REPEATS = 5
times_bf = []
times_dc = []


# Medición experimental de tiempos
def max_subarray_bruteforce(arr):
    n = len(arr)
    max_sum = float("-inf")
    start = 0
    end = 0
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum > max_sum:
                max_sum = current_sum
                start = i
                end = j
    return start, end, max_sum


# Divide y vencerás O(n log n) algoritmo
def max_crossing_subarray(arr, low, mid, high):
    left_sum = float("-inf")
    total = 0
    max_left = mid
    for i in range(mid, low - 1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total
            max_left = i

    right_sum = float("-inf")
    total = 0
    max_right = mid + 1
    for j in range(mid + 1, high + 1):
        total += arr[j]
        if total > right_sum:
            right_sum = total
            max_right = j

    return max_left, max_right, left_sum + right_sum


def max_subarray_divide_and_conquer(arr, low, high):
    if low == high:
        return low, high, arr[low]
    mid = (low + high) // 2
    left_low, left_high, left_sum = max_subarray_divide_and_conquer(
        arr, low, mid)
    right_low, right_high, right_sum = max_subarray_divide_and_conquer(
        arr, mid + 1, high)
    cross_low, cross_high, cross_sum = max_crossing_subarray(
        arr, low, mid, high)
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


test_array = [1, -6, 6, -1, 1, -3, 7, -7, 6, -6]
print("=" * 60)
print("VERIFICACIÓN CON ARREGLO DEL LABORATORIO")
print("=" * 60)
print(f"Arreglo: {test_array}")

low_bf, high_bf, sum_bf = max_subarray_bruteforce(test_array)
print(f"\nFuerza bruta:")
print(f"  Subarreglo: {test_array[low_bf:high_bf+1]}")
print(f"  Índices: [{low_bf}..{high_bf}]")
print(f"  Suma: {sum_bf}")

low_dc, high_dc, sum_dc = max_subarray_divide_and_conquer(
    test_array, 0,
    len(test_array) - 1)
print(f"\nDivide y vencerás:")
print(f"  Subarreglo: {test_array[low_dc:high_dc+1]}")
print(f"  Índices: [{low_dc}..{high_dc}]")
print(f"  Suma: {sum_dc}")

print(f"\nResultados coinciden: {sum_bf == sum_dc}")

SIZES = [10, 50, 100, 200, 500, 1000]
REPEATS = 5
times_bf = []
times_dc = []

print("\n" + "=" * 60)
print("MEDICIÓN DE TIEMPOS DE EJECUCIÓN")
print("=" * 60)
print(f"{'n':>6}  {'Fuerza Bruta (s)':>18}  {'Divide y Vencerás (s)':>22}")
print("-" * 52)

for n in SIZES:
    total_bf = 0.0
    total_dc = 0.0
    for _ in range(REPEATS):
        arr = [random.randint(-100, 100) for _ in range(n)]
        start_time = time.perf_counter()
        max_subarray_bruteforce(arr)
        total_bf += time.perf_counter() - start_time
        start_time = time.perf_counter()
        max_subarray_divide_and_conquer(arr, 0, n - 1)
        total_dc += time.perf_counter() - start_time
    avg_bf = total_bf / REPEATS
    avg_dc = total_dc / REPEATS
    times_bf.append(avg_bf)
    times_dc.append(avg_dc)
    print(f"{n:>6}  {avg_bf:>18.6f}  {avg_dc:>22.6f}")

sns.set_theme(style="whitegrid", palette="muted")
fig, ax = plt.subplots(figsize=(10, 6))
sns.set_theme(style="whitegrid", palette="muted")
fig, ax = plt.subplots(figsize=(10, 6))

# Gráficas
ax.plot(SIZES,
        times_bf,
        marker="o",
        linewidth=2,
        markersize=7,
        label="Fuerza bruta — O(n²)",
        color="#ef4444")
ax.plot(SIZES,
        times_dc,
        marker="s",
        linewidth=2,
        markersize=7,
        label="Divide y vencerás — O(n log n)",
        color="#4a9eed")
ax.set_title("Subarreglo Máximo: Fuerza Bruta vs Divide y Vencerás",
             fontsize=14,
             fontweight="bold",
             pad=15)
ax.set_xlabel("Tamaño de entrada (n)", fontsize=12)
ax.set_ylabel("Tiempo de ejecución promedio (segundos)", fontsize=12)
ax.legend(fontsize=11)
ax.set_xticks(SIZES)
plt.tight_layout()
plt.savefig("grafica_ejercicio3.png", dpi=150, bbox_inches="tight")
plt.show()
print("\nGráfica guardada como: grafica_ejercicio3.png")
