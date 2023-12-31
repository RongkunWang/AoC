#include <iostream>
#include <fstream>
#include <string>

#include <map>
#include <regex>
#include <charconv>
#include <system_error>

#include "util.h"

bool parse(std::map<std::string, std::uint16_t>& cached, const std::string& wire, const std::string& eq) {
  std::smatch match;
  std::regex reg("([a-z0-9]*)( |)([A-Z]*)( |)([a-z0-9]*)");
  std::regex_search(eq, match, reg);
  std::string lh(match[1]), op(match[3]), rh(match[5]);

  bool lvalid{}, rvalid{};
  std::uint16_t numlh{}, numrh{};

  rvalid = std::from_chars(rh.data(), rh.data() + rh.size(), numrh).ec == std::errc{};
  if (cached.find(rh) != cached.end()) {
    numrh = cached[rh];
    rvalid = true;
  }

  lvalid = std::from_chars(lh.data(), lh.data() + lh.size(), numlh).ec == std::errc{};
  if (cached.find(lh) != cached.end()) {
    numlh = cached[lh];
    lvalid = true;
  }

  // if(op == "") {
    // std::cout << eq << std::endl;
    // std::cout << wire << "=" << lh << " " << op << " " << rh << std::endl;
    // std::cout << wire << "=" << numlh << " " << op << " " << numrh << std::endl;
    // std::cout  << std::endl;
  // }

  // NOT never followed by number
  if (op == "NOT" && rvalid) {
    cached[wire] = 65535 - cached[rh];
  } else if (op == "LSHIFT" && lvalid) {
    cached[wire] = numlh << numrh;
  } else if (op == "RSHIFT" && lvalid) {
    cached[wire] = numlh >> numrh;
  } else if (op == "AND" && lvalid && rvalid) {
    cached[wire] = numlh & numrh;
  } else if (op == "OR" && lvalid && rvalid) {
    cached[wire] = numlh | numrh;
  } else if (op == "" && rvalid) {
    cached[wire] = numrh;
  } else if (op == "" && lvalid) {
    cached[wire] = numlh;
  } else {
    return false;
  }

  return true;
}

int main(int argc, char** argv) {

  std::ifstream inFile("input2015/7.txt");

  std::map<std::string, std::string> operations, operations2;
  std::map<std::string, std::uint16_t> cached, cached2;

  std::string line;
  while(getline(inFile, line)) {
    std::smatch match;
    std::regex in_regex("(.*) (->) (\\w+)");
    std::regex_search(line, match, in_regex);
    std::string inputOp(match[1]), wire(match[3]);
    
    operations[wire] = inputOp;
    operations2[wire] = inputOp;
  }


  while (operations.size()) {
    for (const auto & [wire, eq] : operations) {
      if(parse(cached, wire, eq)){
        operations.erase(wire);
        break;
      }
    }
  }


  std::cout << cached["a"] << std::endl;

  operations2.erase("b");
  cached2["b"] = cached["a"];

  while (operations2.size()) {
    for (const auto & [wire, eq] : operations2) {
      if(parse(cached2, wire, eq)){
        operations2.erase(wire);
        break;
      }
    }
  }

  std::cout << cached2["a"] << std::endl;


}

