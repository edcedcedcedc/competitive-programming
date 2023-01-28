#include <iostream>
#include <cmath>

int main()
{
    int m, n, r;
    const int d = 2;
    std::cin >> m >> n;
    r = std::floor(m * n / 2);
    std::cout << r << std::endl;
    return 0;
}
