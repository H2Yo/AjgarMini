from pathlib import Path
import glob

a = glob.glob("./**/*.*",recursive= True)
b= []

for i in a:
    if Path(i).is_file() and Path(i).parent != Path("./Photos-Reorganized"):
        # print(Path(i).parent)
        b.append(Path(i).suffix)
        # b.append(i)

print(set(b))
