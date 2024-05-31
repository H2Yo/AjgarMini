from pathlib import Path
import glob

a = glob.glob("./**/*.jpg",recursive= True)
b= []
c= []

for i in a:
    if Path(i).is_file() and Path(i).parent != Path("./Photos-Reorganized"):
        b.append(Path(i).name)
    elif Path(i).is_file() and Path(i).parent == Path("./Photos-Reorganized"):
        c.append(Path(i).name)


d = [x for x in c if x not in b]
print(*d)
