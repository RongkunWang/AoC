#include <iostream>
#include <fstream>
#include <string>

#include <vector>
#include <regex>
#include <charconv>
#include <array>
#include <numeric>

int main(int argc, char** argv) {

  std::ifstream inFile("input2015/9.txt");

  std::vector<std::string> loc;

  // seems to be less than 50 locations
  std::array<std::array<int, 50>, 50> dis{};

  std::string line;
  int sol1(999999999), sol2(0);
  while(getline(inFile, line)) {
    std::regex re("([A-Za-z]+) to ([A-Za-z]+) = ([0-9]+)");
    std::smatch m;
    std::regex_search(line, m, re);

    std::string s1(m[1]), s2(m[2]), nums(m[3]);
    auto it1 = std::find(loc.begin(), loc.end(), s1);
    int i1 = it1 - loc.begin();
    if (it1 == loc.end()) {
      loc.push_back(s1);
      i1 = loc.size() - 1;
    }

    auto it2 = std::find(loc.begin(), loc.end(), s2);
    int i2 = it2 - loc.begin();
    if (it2 == loc.end()) {
      loc.push_back(s2);
      i2 = loc.size() - 1;
    }

    int d;
    std::from_chars(nums.data(), nums.data() + nums.size(), d);

    // std::cout << s1 << " " << s2 << " " << i1 << " " << i2 << " " << d << std::endl;

    dis[i1][i2] = d;
    dis[i2][i1] = d;
  }

  // for (int i = 0; i < 50; ++i)
    // for (int j = 0; j < 50; ++j)
      // std::cout << i <<  " " << j << " " << dis[i][j] << std::endl;

  // std::cout << dis[0].size() << std::endl;
  // dis[0][0];
  // std::cout << dis[0][1] << std::endl;
 

  // return 0;

  int nCity = loc.size();

  // DFS starting from every city
  // DFS stop at every city, too
  for (int i = 0; i < nCity; ++i) {
    for (int j = i+1; j < nCity; ++j) {
      std::vector<std::vector<int>> paths{ {i}, };
      while (paths.size()) {
        auto visited = paths.back();
        paths.pop_back();

        if (visited.back() == j) {
          int sum(0);
          for (int cur=0; cur < nCity-1; ++cur) {
            sum += dis[visited[cur]][visited[cur+1]];
          }
          sol1 = std::min(sol1, sum);
          sol2 = std::max(sol2, sum);
          continue;
        }

        for (int next = 0; next < nCity; ++next) {
          // skip j if it's not the last
          if (next == j && visited.size() +1 != nCity) continue;
          // skip if already visited once
          if (find(visited.begin(), visited.end(), next) != visited.end()) continue;

          std::vector<int> move_next(visited);
          move_next.push_back(next);
          paths.push_back(std::move(move_next));
        }
      }
    }
  }

  std::cout << sol1 << std::endl;
  std::cout << sol2 << std::endl;

}

