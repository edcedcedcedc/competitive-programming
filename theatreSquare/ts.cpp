#include <iostream>

int main()
{
    long long int a, m, n, i = 1, j = 1, x, y, r;
    std::cin >> m >> n >> a;
    const long long int fA = a * a;
    x = a;
    y = a;
    while (x < n)
    {
        x = a * i;
        i++;
    }
    while (y < m)
    {
        y = a * j;
        j++;
    }
    r = x * y / fA;
    std::cout << r << std::endl;
    return 0;
}