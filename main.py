import cProfile
import pstats

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def main():
    a = 10
    b = 20
    c = 30
    d = 40

    add_result = add(a, b)
    multiply_result = multiply(c, d)

    print(f"Addition result: {add_result}")
    print(f"Multiplication result: {multiply_result}")

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats(10)
```

Kodni profiling qilish uchun quyidagilar qilish kerak:

1. `cProfile` modulini import qiling.
2. Profiling qilish uchun `cProfile.Profile()` obyektini yarat.
3. Profilingni qo'llab-quvvatlash uchun `profiler.enable()` metodi orqali aktiv qiling.
4. Profiling qilish uchun `main()` funksiyasini chaqiring.
5. Profilingni to'xtatish uchun `profiler.disable()` metodi orqali to'xtating.
6. Profiling natijalarini olish uchun `pstats.Stats()` obyektini yarat.
7. Profiling natijalarini sortlash uchun `stats.sort_stats('cumulative')` metodi orqali sortlang.
8. Profiling natijalarini chiqarish uchun `stats.print_stats(10)` metodi orqali chiqaring.
