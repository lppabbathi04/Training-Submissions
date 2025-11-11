import os
import numpy as np

# ✅ Use your correct folder path
folder = r"C:\Users\pabba\Downloads"

# ✅ Check if folder exists
if not os.path.exists(folder):
    print(" Folder not found! Check the path.")
else:
    files = os.listdir(folder)
    sizes = []

    for f in files:
        path = os.path.join(folder, f)
        if os.path.isfile(path):
            try:
                sizes.append(os.path.getsize(path))  # size in bytes
            except:
                print(f"⚠️ Could not read size for file: {f}")

    if len(sizes) == 0:
        print("⚠️ No files found or accessible in folder.")
    else:
        sizes = np.array(sizes)

        print(" Total Files:", len(sizes))
        print(" Average File Size:", np.mean(sizes), "bytes")
        print(" Largest File Size:", np.max(sizes), "bytes")
        print(" Smallest File Size:", np.min(sizes), "bytes")

