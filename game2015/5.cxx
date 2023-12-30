#include <iostream>
#include <fstream>
#include <string>

#include <vector>
#include <algorithm>

bool isNice2(std::string line) {
  bool req1(false), req2(false);
  for (std::size_t i = 0; i < line.size() - 1; ++i) {
    auto sub = line.substr(i, 2);
    if (line.substr(i+2, line.size() - i - 2).find(sub) != std::string::npos) {
      req1 = true;
    }
    if (i < line.size() - 2 and line[i] == line[i+2]) {
      req2 = true;
    }
  }

  return req1 && req2;
}


bool isNice1(std::string line) { 
  bool illegal = false;
  for(const auto & sub : std::vector<std::string> {"ab", "cd", "pq", "xy"}) {
    if (line.find(sub) != std::string::npos) {
      illegal = true;
      break;
    }
  }

  if (illegal) return false;

  bool require = false;
  for (char c = 'a'; c <= 'z'; ++c) {
    std::string single_c{c};
    std::string sub(single_c+single_c);
    if (line.find(sub) != std::string::npos) {
      require = true;
      break;
    }
  }

  if (!require) return false;

  auto vow = std::count_if(line.begin(), line.end(), 
      [](const char c){return std::string("aeiou").find(c) != std::string::npos;});

  return vow >= 3;

}

int main(int argc, char** argv) {

  std::ifstream inFile("game2015/5.txt");

  std::string line;
  int sol1(0), sol2(0);
  while(inFile >> line) {
    if (isNice1(line)) ++sol1;
    if (isNice2(line)) ++sol2;

  }

  std::cout << sol1 << std::endl;
  std::cout << sol2 << std::endl;

}
