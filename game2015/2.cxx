#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <string_view>
#include <ranges>
#include <charconv>
#include <algorithm>
#include <numeric>

int main(int argc, char** argv) {

  std::ifstream inFile("game2015/2.txt");

  std::string line;
  int paper(0), ribbon(0);
  while(inFile >> line) {
    auto split = line 
      | std::ranges::views::split('x')
      | std::ranges::views::transform([](auto&& str) { return std::string_view(&*str.begin(), std::ranges::distance(str)); });

    int dimI[3];
    int i = 0;
    for (auto &&dim : split) {
      std::from_chars(dim.data(), dim.data() + dim.size(), dimI[i]);
      ++i;
    }
    int area[3] = {dimI[0] * dimI[1], dimI[1] * dimI[2], dimI[2] * dimI[0]};
    int halfCirc[3] = {dimI[0] + dimI[1], dimI[1] + dimI[2], dimI[2] + dimI[0]};
    paper  += 2 * (area[0] + area[1] + area[2]) 
      + *std::min_element(area, area+3); // slack
    ribbon += 2 * *std::min_element(halfCirc, halfCirc+3) 
      + std::accumulate(std::begin(dimI), std::end(dimI), 1, std::multiplies<int>()); // bow

  }
  std::cout << paper << std::endl;
  std::cout << ribbon << std::endl;

  return 0;
}
