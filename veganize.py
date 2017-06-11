import shutil
import os.path
import re

def copy_files_with_replace(src, replacements, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.makedirs(dest)
    filenames = os.listdir(src)
    for filename in filenames:
        src_path = os.path.join(src, filename)
        dest_path = os.path.join(dest, filename)
        with open(src_path, "r") as in_file:
            data = in_file.read()
        for (regex, subst) in replacements:
            result = re.sub(regex, subst, data, 0)
            if result:
                data = result
        with open(dest_path, "w") as out_file:
            out_file.write(data)
            out_file.close()

food_replacements = [
    (r"0xA70D623E[^>]*>", '0x3D94FDEF<!--Avocado Toast-->')
]

if __name__ == "__main__":
    copy_files_with_replace('SampleInputs', food_replacements, 'Outputs')
