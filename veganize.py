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
            src_data = in_file.read()

        replaced_data = src_data
        for (regex, subst) in replacements:
            replaced_data = re.sub(regex, subst, replaced_data, 0)

        if src_data != replaced_data:
            with open(dest_path, "w") as out_file:
                out_file.write(replaced_data)
                out_file.close()


def apply_renames(src, renames, dest):
    replacements = []
    for (old_hash, old_name, new_hash, new_name) in renames:
        regex = r"" + old_hash + r"[^>]*>"
        subst = new_hash + '<!-- ' + new_name + ' -->'
        replacements.append((regex, subst))
    copy_files_with_replace(src, replacements, dest)

food_renames = [
    ('0xA70D623E', 'Eggs and Toast', '0x3D94FDEF', 'Avocado Toast')
]

if __name__ == "__main__":
    # copy_files_with_replace('SampleInputs', food_replacements, 'Outputs')
    apply_renames('SampleInputs', food_renames, 'Outputs')
