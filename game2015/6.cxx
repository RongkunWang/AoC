#include <iostream>
#include <fstream>
#include <string>

#include <algorithm>
#include <array>
#include <regex>

#include "util.h"

int main(int argc, char** argv) {

  std::ifstream inFile("game2015/6.txt");

  std::string line;
  int sol1(0), sol2(0);
  std::array<std::array<bool, 1000>, 1000> light;
  light.fill({});
  std::array<std::array<int, 1000>, 1000> bright;
  std::for_each(bright.begin(), bright.end(), [](auto &c) { std::fill(c.begin(), c.end(), 0); });
  while(getline(inFile, line)) {
    std::smatch in_match;
    std::regex in_regex("(turn off|turn on|toggle) ([0-9]+),([0-9]+) (through) ([0-9]+),([0-9]+)");
    std::regex_search(line, in_match, in_regex);
    auto pos1 = buildComplex(in_match[2], in_match[3]);
    auto pos2 = buildComplex(in_match[5], in_match[6]);

    // std::cout << pos1 << " " << pos2 << std::endl;

    std::string instruction(in_match[1]);
    for (std::size_t r = pos1.real(); r <= pos2.real(); ++r) {
      for (std::size_t c = pos1.imag(); c <= pos2.imag(); ++c) {
        if (in_match[1] == "turn on") {
          light[r][c] = true;
          ++bright[r][c];
        } else if (in_match[1] == "turn off") {
          light[r][c] = false;
          if (bright[r][c] >= 1)
            --bright[r][c];
        } else if (in_match[1] == "toggle") {
          light[r][c] = !light[r][c];
          bright[r][c] += 2;
        } else {
          throw std::invalid_argument("Unexpected instruction.");
        }
      }
    }
  }

  for (std::size_t i = 0; i < 1000; ++i) 
    for (std::size_t j = 0; j < 1000; ++j) {
      if (light[i][j]) ++sol1;
      sol2 += bright[i][j];
    }

  std::cout << sol1 << std::endl;
  std::cout << sol2 << std::endl;

}
