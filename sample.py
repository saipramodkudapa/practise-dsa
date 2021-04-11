import os


def list_files(filepath, filetype):
    paths = []
    patient_dir = os.path.basename(filepath)
    for root, dirs, files in os.walk(filepath):
        for file in files:
            if file.lower().endswith(filetype.lower()):
                internal_path = os.path.join(root, file).split(patient_dir)[1]
                paths.append(internal_path)
    return paths


res = list_files('/Users/pramod/Desktop/dicom-images', '.dcm')
print(res)