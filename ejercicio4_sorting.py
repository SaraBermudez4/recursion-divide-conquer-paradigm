import time
import random
import matplotlib.pyplot as plt
import seaborn as sns


# Merge Sort O(n log n)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


# Insertion Sort O(n^2) worst, O(n) best
def insertion_sort(arr):
    arr = arr.copy()
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr


# Prueba con arreglo de ejemplo
test_array = [1, 6, 6, 1, 1, 3, 7, 7, 6, 6]
print("=" * 60)
print("VERIFICACIÓN CON ARREGLO DEL LABORATORIO")
print("=" * 60)
print(f"Arreglo original: {test_array}")
print(f"Merge Sort:       {merge_sort(test_array)}")
print(f"Insertion Sort:   {insertion_sort(test_array)}")
print(
    f"Resultados coinciden: {merge_sort(test_array) == insertion_sort(test_array)}"
)

# Medición experimental de tiempos
SIZES = [10, 50, 100, 500, 1000, 5000]
REPEATS = 5
times_ms = []
times_is = []

print("\n" + "=" * 60)
print("MEDICIÓN DE TIEMPOS DE EJECUCIÓN")
print("=" * 60)
print(f"{'n':>6}  {'Merge Sort (s)':>16}  {'Insertion Sort (s)':>20}")
print("-" * 48)

for n in SIZES:
    total_ms = 0.0
    total_is = 0.0
    for _ in range(REPEATS):
        arr = [random.randint(-1000, 1000) for _ in range(n)]
        arr_copy = arr.copy()
        start = time.perf_counter()
        merge_sort(arr_copy)
        total_ms += time.perf_counter() - start
        start = time.perf_counter()
        insertion_sort(arr)
        total_is += time.perf_counter() - start
    avg_ms = total_ms / REPEATS
    avg_is = total_is / REPEATS
    times_ms.append(avg_ms)
    times_is.append(avg_is)
    print(f"{n:>6}  {avg_ms:>16.6f}  {avg_is:>20.6f}")

# Gráficas
sns.set_theme(style="whitegrid", palette="muted")
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Gráfica 1 — Escala lineal
axes[0].plot(SIZES,
             times_ms,
             marker="s",
             linewidth=2,
             markersize=7,
             label="Merge Sort — O(n log n)",
             color="#4a9eed")
axes[0].plot(SIZES,
             times_is,
             marker="o",
             linewidth=2,
             markersize=7,
             label="Insertion Sort — O(n²)",
             color="#ef4444")
axes[0].set_title("Escala lineal", fontsize=12, fontweight="bold")
axes[0].set_xlabel("Tamaño de entrada (n)", fontsize=11)
axes[0].set_ylabel("Tiempo de ejecución promedio (s)", fontsize=11)
axes[0].legend(fontsize=10)
axes[0].set_xticks(SIZES)
axes[0].tick_params(axis="x", rotation=30)

# Gráfica 2 — Escala logarítmica
axes[1].plot(SIZES,
             times_ms,
             marker="s",
             linewidth=2,
             markersize=7,
             label="Merge Sort — O(n log n)",
             color="#4a9eed")
axes[1].plot(SIZES,
             times_is,
             marker="o",
             linewidth=2,
             markersize=7,
             label="Insertion Sort — O(n²)",
             color="#ef4444")
axes[1].set_title("Escala logarítmica", fontsize=12, fontweight="bold")
axes[1].set_xlabel("Tamaño de entrada (n)", fontsize=11)
axes[1].set_ylabel("Tiempo de ejecución promedio (s) — log", fontsize=11)
axes[1].set_yscale("log")
axes[1].legend(fontsize=10)
axes[1].set_xticks(SIZES)
axes[1].tick_params(axis="x", rotation=30)
fig.suptitle("Merge Sort vs Insertion Sort — Comparación experimental",
             fontsize=14,
             fontweight="bold",
             y=1.02)
plt.tight_layout()
plt.savefig("grafica_ejercicio4.png", dpi=150, bbox_inches="tight")
plt.show()
print("\nGráfica guardada como: grafica_ejercicio4.png")
