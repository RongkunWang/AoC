#include <iostream>
#include <fstream>
#include <string>

int main(int argc, char** argv) {

  auto toPair = [](const housePos p){ return std::make_pair(p.real(), p.imag());};

  std::ifstream inFile("game2015/4.txt");
  std::string line;
  std::getline(inFile, line);

  return 0;
}

