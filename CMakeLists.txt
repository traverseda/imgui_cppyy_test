cmake_minimum_required(VERSION 3.17)
project(imgui LANGUAGES CXX)

execute_process(COMMAND cling-config --cmake OUTPUT_VARIABLE CPPYY_MODULE_PATH OUTPUT_STRIP_TRAILING_WHITESPACE)
# Make sure this is set to something like:
# ~/.local/lib/python2.7/site-packages/cpyy_backend/cmake 
message("CPYY_MODULE_PATH: " ${CPPYY_MODULE_PATH})
list(INSERT CMAKE_MODULE_PATH 0 ${CPPYY_MODULE_PATH})
find_package(Cppyy)

set(SOURCES imgui/imgui.cpp imgui/imgui_demo.cpp imgui/imgui_draw.cpp imgui/imgui_widgets.cpp)
set(HEADERS imgui/imgui.h)

add_library(imgui SHARED ${SOURCES})
set_target_properties(imgui PROPERTIES POSITION_INDEPENDENT_CODE ON)
target_include_directories(imgui PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

cppyy_add_bindings(
   "imgui" "0.0.1" "traverseda" "traverse.da@gmail.com"
   LANGUAGE_STANDARD "14"
   GENERATE_OPTIONS "-D__PIC__;-Wno-macro-redefined"
   INCLUDE_DIRS ${CMAKE_CURRENT_SOURCE_DIR}/imgui
   LINK_LIBRARIES imgui
   H_DIRS ${CMAKE_CURRENT_SOURCE_DIR}
   H_FILES ${HEADERS})

