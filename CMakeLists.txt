cmake_minimum_required(VERSION 3.20.2)
project(AoCPre2023 DESCRIPTION "all the AOC code I have before 2023. Just for fun. Just for fun.")

find_package(OpenSSL REQUIRED)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_FLAGS "-O3")



set(INCLUDE_DIRS include)
set(HEADER_FILES include/util.h)

add_library(aocUtilLib SHARED
    src/util.cxx
    ${HEADER_FILES}
)

target_include_directories(aocUtilLib PRIVATE include)


foreach( exec 2 3 4 5 6 )
    add_executable ( 2015.${exec} game2015/${exec}.cxx)
    target_include_directories(2015.${exec} PRIVATE ${INCLUDE_DIRS})
    target_link_libraries(2015.${exec} aocUtilLib)
    if (${exec} EQUAL 4)
        target_link_libraries(2015.${exec} OpenSSL::Crypto)
    endif()
endforeach()

