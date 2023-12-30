#ifndef AOCUTIL_RKRKRK
#define AOCUTIL_RKRKRK
#include <complex>
#include <utility>

typedef std::complex<int> Pos;
auto complexToPair = [](const Pos p){ return std::make_pair(p.real(), p.imag());};

Pos buildComplex(const std::string& sr, const std::string & si);


#endif
