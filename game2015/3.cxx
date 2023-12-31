#include <iostream>
#include <fstream>
#include <string>

#include <complex>
#include <map>
#include <vector>
#include <set>
#include <iterator>
#include <algorithm>


#include "util.h"

int main(int argc, char** argv) {

  using namespace std::complex_literals;
  std::map<char, Pos> moveMap({ {'>', 1}, {'^', 1i}, {'v', -1i}, {'<', -1} });

  std::ifstream inFile("input2015/3.txt");
  std::string line;
  std::getline(inFile, line);


  std::vector<Pos> visited(1, 0);
  Pos santa(0), roboSanta(0);
  std::set<std::pair<int, int>> thisYear({{0, 0}});
  bool santaMove = true;
  for(char& c : line) {
    visited.push_back(visited.back() + moveMap[c]);
    if (santaMove) {
      santa += moveMap[c];
      thisYear.insert(complexToPair(santa));
    } else { 
      roboSanta += moveMap[c];
      thisYear.insert(complexToPair(roboSanta));
    }
    santaMove = !santaMove;
  }


  std::set<std::pair<int, int>> uniqueVisited;
  std::transform(visited.begin(), visited.end(), std::inserter(uniqueVisited, uniqueVisited.end()), complexToPair);
  std::cout << uniqueVisited.size() << std::endl;
  std::cout << thisYear.size() << std::endl;


  return 0;
}
