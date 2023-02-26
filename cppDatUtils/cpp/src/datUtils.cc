// #include <dlib/clustering.h>
#include <dlib/dnn.h>
#include <dlib/image_io.h>
#include <dlib/string.h>

#include "datUtils.h"

void validateDeserialization(string output_path) {
  dlib::deserialize(output_path);
}
string deserializeFaceDescriptors(string dat_file_path) {
  // Load the serialized data from a .dat file
  std::vector<dlib::matrix<float, 0, 1>> hashes_matrix;
  std::ifstream input(dat_file_path, std::ios::binary);
  dlib::deserialize(hashes_matrix, input);

  // Convert the loaded data to a string of groups of 128 floats
  std::ostringstream ss;
  int counter = 0;
  for (const auto &matrix : hashes_matrix) {
    for (const auto &val : matrix) {
      if (counter % 128 == 0) {
        ss << "[";
      }
      ss << val;
      if (counter % 128 == 127) {
        ss << "],";
      } else {
        ss << ",";
      }
      counter++;
    }
  }

  std::string floatString = ss.str();
  // Remove the trailing comma
  floatString.pop_back();

  // std::cout << "Float string: " << floatString << std::endl;

  return floatString;
}
string deserializeFaceNames(string dat_file_path) {
  std::vector<std::string> ids;
  std::ifstream input(dat_file_path, std::ios::binary);
  dlib::deserialize(ids, input);

  // Convert the loaded data to a string with each element enclosed in quotes
  // and separated by commas
  std::ostringstream ss;
  ss << "[";
  for (auto it = ids.begin(); it != ids.end(); ++it) {
    ss << "\"" << *it << "\"";
    if (it != ids.end() - 1) {
      ss << ",";
    }
  }
  ss << "]";

  return ss.str();
}

void saveIds(const vector<string> ids, string output_path) {
  dlib::serialize(output_path) << ids;
}

void saveHashes(const vector<string> hashes, string output_path) {
  std::vector<dlib::matrix<float, 0, 1>> hashes_matrix;
  for (auto &hash : hashes) {
    std::vector<float> local_encodings;
    std::stringstream ss(hash);
    while (ss.good()) {
      string substr;
      getline(ss, substr, ',');

      local_encodings.push_back(stof(substr));
    }

    dlib::matrix<float> one_encoding(128, 1);

    for (size_t k = 0; k <= 127; k++) {
      one_encoding(k - 1, 1) = local_encodings[k];
    }
    hashes_matrix.push_back(one_encoding);
  }
  dlib::serialize(output_path) << hashes_matrix;

  validateDeserialization("output_path");
}