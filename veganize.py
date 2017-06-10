import shutil
import os.path
import re

def copy_files_with_replace(src, filenames, dest):
    for (filename, regex, subst) in filenames:
        src_path = os.path.join(src, filename)
        dest_path = os.path.join(dest, filename)
        with open (src_path, "r") as myfile:
            data = myfile.read()
            result = re.sub(regex, subst, data, 0)
            if result:
                with open (dest_path, "w") as outfile:
                    outfile.write(result)

food_filenames = [
    ('EB97F823!00000000!0000000000007EB8.recipe_Food_Homestyle_EggsToast-Single.RecipeTuning.xml', r"0xA70D623E[^>]*>", '0x3D94FDEF<!--Avocado Toast-->')
]

if __name__ == "__main__":
    copy_files_with_replace('SampleInputs', food_filenames, 'Outputs')
