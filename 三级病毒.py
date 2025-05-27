data = []
try:
    while True:
        print("分配 1GB...")
        data.append(bytearray(10 * 1024 * 1024 * 1024))  # 每次 10GB
except MemoryError:
    print("内存已耗尽！")
