#include <iostream>
#include <fstream>
#include <string>

int main(int argc, char** argv) {

  std::ifstream inFile("input2015/8.txt");

  std::string line;
  int sol1(0), sol2(0);
  while(getline(inFile, line)) {

    // it seems that \ is always followed by \, " or x. the previous two cases it's expended twice, so 2-->4. the x cases, 4 char --> 5 char.
    std::size_t count(0), pos(1), count2(6);
    // make sure the double quotes will be skipped when counting reduced
    while (pos < line.size() - 1) {
      if (line[pos] != '\\' || (line[pos] == '\\' && pos == line.size() - 2)) {
        ++count;
        count2 += 1;
        ++pos;
      } else if (line[pos+1] != 'x') {
        // when this \ is escape
        ++count;
        count2 += 4;
        pos += 2;
      } else {
        // when this \ is followed by x. Skip +1(x) and +2, +3(two hex)
        ++count;
        count2 += 5;
        pos += 4;
      }
    }
    sol1 += line.size() - count;
    sol2 += count2 - line.size();
  }

  std::cout << sol1 << std::endl;
  std::cout << sol2 << std::endl;

}
