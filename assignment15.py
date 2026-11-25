
import gc
import tracemalloc
tracemalloc.start()

gc.disable()

print("Garbage collection thresholds:", gc.get_threshold())

objects = []

for i in range(10000):
    a = []
    b = []
    a.append(b)
    b.append(a)
    objects.append(a)

current, peak = tracemalloc.get_traced_memory()
print("\nMemory before deletion:", current, "bytes")

del objects

current, peak = tracemalloc.get_traced_memory()
print("Memory before garbage collection:", current, "bytes")

collected = gc.collect()

current, peak = tracemalloc.get_traced_memory()
print("Memory after garbage collection:", current, "bytes")

print("\nGarbage objects collected:", collected)
gc.enable()

tracemalloc.stop()

print("\nManual garbage collection completed successfully!")
