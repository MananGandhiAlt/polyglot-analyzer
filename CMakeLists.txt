cmake_minimum_required(VERSION 3.5)
project(word_counter)

set(CMAKE_CXX_STANDARD 14)  # BUG: code uses C++17 features

add_executable(word_counter src/word_counter.cpp)
