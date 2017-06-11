import shutil
import os.path
import re
from fnvhash import fnv1_32

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


def calculate_hash(phrase):
    lower_case = phrase.lower()
    hashed = hex(fnv1_32(bytes(lower_case, 'utf-8'))).upper()
    return '0x' + hashed[2:]

def find_hash(src, phrase):
    filenames = os.listdir(src)
    for filename in filenames:
        src_path = os.path.join(src, filename)

        with open(src_path, "r") as in_file:
            src_data = in_file.read()

        regex = r"(0x[0-9A-F]{8})<!--\s?" + phrase + "\s?-->"

        matches = re.finditer(regex, src_data)

        for matchNum, match in enumerate(matches):
            return match.groups()[0]


def apply_renames(src, renames, dest):
    replacements = []
    for (old_name, new_name) in renames:
        old_hash = find_hash(src, old_name)
        new_hash = calculate_hash(new_name)
        regex = r"" + old_hash + r"[^>]*>"
        subst = new_hash + '<!-- ' + new_name + ' -->'
        replacements.append((regex, subst))
    copy_files_with_replace(src, replacements, dest)

food_renames = [
    ('Eggs and Toast', 'Avocado Toast')
]

if __name__ == "__main__":
    apply_renames('SampleInputs', food_renames, 'Outputs')
