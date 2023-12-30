#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

#include <openssl/md5.h>

int main(int argc, char** argv) {


  unsigned char result[MD5_DIGEST_LENGTH];

  std::string line("iwrupvqb");

  int i(-1), out(0);
  int sol1 = 0;
  do {
    std::stringstream ss;
    ++i;
    ss << line << i;
    auto example = ss.str();
    MD5((unsigned char*)example.c_str(), example.size(), result);
    out = (static_cast<int>( result[0] ) << 16) + (static_cast<int>( result[1] ) << 8) + static_cast<int>( result[2] );
    if (sol1 == 0 && (out >> 4) == 0) sol1 = i;
  } while(out != 0);

  std::cout << sol1 << std::endl;
  std::cout << i << std::endl;

  return 0;
}

