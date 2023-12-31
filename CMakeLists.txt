cmake_minimum_required(VERSION 3.20.2)
project(AoCPre2023 DESCRIPTION "all the AOC code I have before 2023. Just for fun. Just for fun.")

find_package(OpenSSL REQUIRED)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_FLAGS "-O3")

set(CMAKE_INSTALL_PREFIX ${CMAKE_CURRENT_BINARY_DIR})
# string(replace " " "\ " CMAKE_INSTALL_PREFI ${CMAKE_INSTALL_PREFI_pre})



set(INCLUDE_DIRS include)
set(HEADER_FILES include/util.h)

add_library(aocUtilLib SHARED
    src/util.cxx
    ${HEADER_FILES}
)

target_include_directories(aocUtilLib PRIVATE include)



foreach( year 2015 )
    set(gameDir "game${year}")
    file(GLOB exe "${gameDir}/*.cxx")
    file(GLOB input "${gameDir}/*.txt")

    foreach( exeFullPath ${exe} )
        get_filename_component(exec ${exeFullPath} NAME_WLE)
        message(STATUS "${year} Day${exec}")
        set(exeName ${year}.${exec})
        add_executable ( ${exeName} ${gameDir}/${exec}.cxx)
        target_include_directories(${exeName} PRIVATE ${INCLUDE_DIRS})
        target_link_libraries(${exeName} aocUtilLib)
        if (${year} EQUAL ${year} AND ${exec} EQUAL 4)
            target_link_libraries(${exeName} OpenSSL::Crypto)
        endif()
    endforeach()
    install(DIRECTORY DESTINATION input${year})
    install(FILES ${input} DESTINATION input${year}/)
endforeach()
