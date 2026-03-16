import os 
folder = "./"
total_size = 0

for file in os.listdir(folder):
    path = os.path.join(folder, file)
    if os.path.isfile(path):
        total_size += os.path.getsize(path)

print("Total size:", total_size, "bytes")