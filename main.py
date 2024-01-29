files = {'1.txt': 0, '2.txt': 0, '3.txt': 0}
file_sizes = []

for file in files:
    with open(file, encoding='utf8') as f:
        size = len(f.readlines())
        files[file] = size
        file_sizes += [size]
file_sizes.sort()

for size in file_sizes:
    for name in files:
        if files[name] == size:
            print(f'{name}\n{size}')
            with open(name, encoding='utf8') as f:
                print(f.read())


