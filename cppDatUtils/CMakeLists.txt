cmake_minimum_required(VERSION 3.19)

project(datUtilsWrapper LANGUAGES CXX)

set(CMAKE_INCLUDE_CURRENT_DIR OFF)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_VISIBILITY_PRESET hidden)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(CONDA_ENV $ENV{CONDA_PREFIX})

list(APPEND CMAKE_PREFIX_PATH ${CONDA_ENV})

include(FetchContent)
FetchContent_Declare(dlib
    GIT_REPOSITORY https://github.com/davisking/dlib.git
    GIT_TAG v19.18
)
FetchContent_MakeAvailable(dlib)

add_compile_definitions(USE_PYTHON_INTERFACE)
find_package(Python COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 CONFIG REQUIRED)

message("pybind11_INCLUDE_DIR ${pybind11_INCLUDE_DIR}")
include_directories(
    ${Python_INCLUDE_DIRS}
    ${pybind11_INCLUDE_DIR}
    ${dlib_SOURCE_DIR}
    cpp/include
)

add_library(datUtils STATIC
    cpp/src/datUtils.cc
    cpp/include/datUtils.h
)

target_include_directories(datUtils PUBLIC cpp/include)

pybind11_add_module(dat_utils_wrapper MODULE pybind11/datUtilsWrapper.cc)

target_link_libraries(dat_utils_wrapper PUBLIC datUtils dlib::dlib)

message("Python_INCLUDE_DIRS ${Python_INCLUDE_DIRS}")
message("Python_SITELIB ${Python_SITELIB}")

# install(DIRECTORY python/dat_utils_wrapper DESTINATION "${Python_SITELIB}")
install(TARGETS dat_utils_wrapper DESTINATION "${Python_SITELIB}/dat_utils_wrapper")