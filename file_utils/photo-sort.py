
from pathlib import Path
import shutil
from datetime import datetime

log_path = Path(f"./year_locate_log_{datetime.now().strftime('%Y%m%d__%H_%M_%S')}.txt")

# find files that start with imgxxxx and place it in folder xxxx  ; xxxx --> year
with open(log_path, "a") as log_obj :
    for sr_no,file_path in enumerate(Path("./Photos-Reorganized").glob(pattern = "./20[0-9][0-9]*.jpg")) :
        
        this_year =  file_path.name[0:4]
        # this_year = "kerala_trip_clg"
        Path.mkdir(file_path.parent / this_year ,exist_ok=True)
        shutil.move(file_path, file_path.parent / this_year)
        log_obj.write(f"""
{file_path} written to {file_path.parent / this_year}
Details
----------------------------------
file_path = {file_path}
file_path.parent = {file_path.parent}, {type(file_path.parent)}
this_year = {this_year}
file_path.parent / this_year = {file_path.parent / this_year}
===================================""")

print("log_file_name is " + str(log_path.name))
