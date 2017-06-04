import shutil
import os.path

def copy_files(src, filenames, dest):
    for filename in filenames:
        src_path = os.path.join(src, filename)
        dest_path = os.path.join(dest, filename)
        shutil.copyfile(src_path, dest_path)

food_filenames = [
    'EB97F823!00000000!0000000000007EB8.recipe_Food_Homestyle_EggsToast-Single.RecipeTuning.xml'
]

if __name__ == "__main__":
    copy_files('SampleInputs', food_filenames, 'Outputs')
