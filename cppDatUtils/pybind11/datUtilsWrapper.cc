#include <string>

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "datUtils.h"

namespace py = pybind11;


PYBIND11_MODULE(dat_utils_wrapper, m) {
    m.doc() = "generate dat";

    m.def("save_ids", &saveIds);
    m.def("save_hashes", &saveHashes);
    m.def("validate_serialization", &validateDeserialization);
    m.def("deserialize_face_descriptors", &deserializeFaceDescriptors);
    m.def("deserialize_face_names", &deserializeFaceNames);
}