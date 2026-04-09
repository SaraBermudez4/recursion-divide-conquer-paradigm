# 📊 Laboratorio 1 — Análisis de Algoritmos

## 📖 Descripción

Implementaciones en Python del Laboratorio #1 de la asignatura **Análisis de Algoritmos**
de la Ingeniería en Sistemas — Institución Universitaria ITM.

El laboratorio analiza y compara experimentalmente algoritmos basados en **recursividad**
y el paradigma **divide y vencerás**, midiendo tiempos de ejecución para diferentes tamaños
de entrada y generando gráficas comparativas.

|                        |                                 |
| ---------------------- | ------------------------------- |
| 👨‍🏫 **Docente**          | Santiago Suarez Cortes          |
| 🧑‍🎓 **Estudiante**       | Sara Estefania Bermudez Alvarez |
| 📅 **Fecha de entrega** | 18 de Abril de 2026             |
| 🐍 **Lenguaje**         | Python 3                        |

---

## 📁 Estructura del repositorio

```
📦 Laboratorio1-AnalisisAlgoritmos
 ┣ 📜 ejercicio3_subarreglo_maximo.py   # Fuerza bruta vs. divide y vencerás
 ┣ 📜 ejercicio4_sorting.py             # Merge Sort vs. Insertion Sort
 ┣ 📁 graficas/
 ┃ ┣ 🖼️  grafica_ejercicio3.png          # Gráfica comparativa ejercicio 3
 ┃ ┗ 🖼️  grafica_ejercicio4.png          # Gráfica comparativa ejercicio 4
 ┗ 📄 README.md
```

---

## 🧪 Ejercicios implementados

### Ejercicio 3 — Problema del Subarreglo Máximo
Compara dos algoritmos para encontrar el subarreglo contiguo de suma máxima:

- 🔴 **Fuerza bruta** → O(n²)
- 🔵 **Divide y vencerás** → O(n log n)

Tamaños evaluados: `n = 10, 50, 100, 200, 500, 1000`

### Ejercicio 4 — Algoritmos de Ordenamiento
Compara dos algoritmos de ordenamiento:

- 🔵 **Merge Sort** → O(n log n)
- 🔴 **Insertion Sort** → O(n²) peor caso

Tamaños evaluados: `n = 10, 50, 100, 500, 1000, 5000`

---

## 🛠️ Tecnologías utilizadas

- Python 🐍 (v3.x)
- Matplotlib 📈 (generación de gráficas)
- Seaborn 🎨 (estilo de gráficas)

---

## 🚀 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/laboratorio1-analisis-algoritmos.git
   cd laboratorio1-analisis-algoritmos
   ```

2. Instala las dependencias:
   ```bash
   pip install matplotlib seaborn
   ```

---

## ▶️ Ejecución

Ejercicio 3 — Subarreglo máximo:
```bash
python3 ejercicio3_subarreglo_maximo.py
```

Ejercicio 4 — Ordenamiento:
```bash
python3 ejercicio4_sorting.py
```

Cada script imprime los tiempos de ejecución en consola y guarda automáticamente
su gráfica comparativa en la carpeta `graficas/`. 📊