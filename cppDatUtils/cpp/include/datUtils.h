#pragma once

#include <string>
#include <vector>

using namespace std;

void saveIds(const vector<string> ids, string output_path);

void saveHashes(const vector<string> hashes, string output_path);

void validateDeserialization(string output_path);

string deserializeFaceDescriptors(string dat_path);

string deserializeFaceNames(string output_path);
