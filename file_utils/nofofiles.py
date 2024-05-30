from pathlib import Path

# a = [x for x in  Path(".").iterdir()]

# for i in a:
#     print(i.is_dir())


print(*[x for x in Path(".").glob("./**/*.py",recursive =True)])