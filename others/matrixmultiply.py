#Czy zmiana kolejności indexów wpływa na długość:
import random
import time

# Funkcja do tworzenia losowej macierzy SIZE x SIZE
def random_matrix(size):
    return [[random.random() for _ in range(size)] for _ in range(size)]

# 6 wersji mnożenia macierzy różniących się kolejnością pętli
def multiply_ijk(A, B, size):
    C = [[0.0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                C[i][j] += A[i][k] * B[k][j]
    return C

def multiply_ikj(A, B, size):
    C = [[0.0] * size for _ in range(size)]
    for i in range(size):
        for k in range(size):
            for j in range(size):
                C[i][j] += A[i][k] * B[k][j]
    return C

def multiply_jik(A, B, size):
    C = [[0.0] * size for _ in range(size)]
    for j in range(size):
        for i in range(size):
            for k in range(size):
                C[i][j] += A[i][k] * B[k][j]
    return C

def multiply_jki(A, B, size):
    C = [[0.0] * size for _ in range(size)]
    for j in range(size):
        for k in range(size):
            for i in range(size):
                C[i][j] += A[i][k] * B[k][j]
    return C

def multiply_kij(A, B, size):
    C = [[0.0] * size for _ in range(size)]
    for k in range(size):
        for i in range(size):
            for j in range(size):
                C[i][j] += A[i][k] * B[k][j]
    return C

def multiply_kji(A, B, size):
    C = [[0.0] * size for _ in range(size)]
    for k in range(size):
        for j in range(size):
            for i in range(size):
                C[i][j] += A[i][k] * B[k][j]
    return C

# Funkcja do pomiaru czasu
def measure_time(func, A, B, size):
    start = time.time()
    func(A, B, size)
    end = time.time()
    return (end - start) * 1000  # w milisekundach

# Główna część programu
if __name__ == "__main__":
    sizes = [10, 100, 1000]

    for size in sizes:
        print(f"\n=== Rozmiar macierzy: {size} x {size} ===")
        A = random_matrix(size)
        B = random_matrix(size)

        results = {
            "ijk": measure_time(multiply_ijk, A, B, size),
            "ikj": measure_time(multiply_ikj, A, B, size),
            "jik": measure_time(multiply_jik, A, B, size),
            "jki": measure_time(multiply_jki, A, B, size),
            "kij": measure_time(multiply_kij, A, B, size),
            "kji": measure_time(multiply_kji, A, B, size),
        }

        for name, t in results.items():
            print(f"{name}: {t:.2f} ms")
