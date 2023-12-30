#include "util.h"
#include <charconv>

Pos buildComplex(const std::string& sr, const std::string& si) {
  int r, i;
  std::from_chars(sr.data(), sr.data() + sr.size(), r);
  std::from_chars(si.data(), si.data() + si.size(), i);

  return {r, i};

}
