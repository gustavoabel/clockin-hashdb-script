import ast
import json
import sys
import os
from typing import List, Dict

from dat_utils_wrapper import deserialize_face_descriptors, deserialize_face_names

def load_data_from_dat(encoding_path: str, names_path: str) -> List[Dict]:
    face_descriptors = deserialize_face_descriptors(encoding_path)
    face_descriptors_list = [sublist for sublist in ast.literal_eval(face_descriptors)]

    face_names = deserialize_face_names(names_path)
    face_names_list = [str(sublist) for sublist in ast.literal_eval(face_names)]

    if len(face_names_list) != len(face_descriptors_list):
        raise Exception("Number of face names does not match number of face descriptors")

    #  Combine face_names and face_descriptors into a list of dictionaries
    face_data = [{'id': name, 'descriptor': descriptor} for name, descriptor in zip(face_names_list, face_descriptors_list)]

    return face_data

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python dat_utils.py ENCODING_PATH NAMES_PATH")
        print('Usage example: python dat_utils.py "/Users/hamiltonmatos/Downloads/git/labs-pocs/clockin-dat-utils/dat-files/face_descriptors_jittered.dat" "/Users/hamiltonmatos/Downloads/git/labs-pocs/clockin-dat-utils/dat-files/face_names_jittered.dat"')
        sys.exit(1)

    encoding_path = sys.argv[1]
    names_path = sys.argv[2]

    try:
        face_data = load_data_from_dat(encoding_path, names_path)

        script_dir = os.path.dirname(os.path.abspath(__file__))

        output_path = os.path.join(script_dir, "src", "data.json")

        with open(output_path, 'w') as f:
            json.dump(face_data, f)
            print("Wrote data.json")

    except Exception as e:
        print("Error: {}".format(e))
