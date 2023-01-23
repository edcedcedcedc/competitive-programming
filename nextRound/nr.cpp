#include <iostream>

int main()
{
    int n, k, i, c = 0;
    std::cin >> n >> k;
    int *p = new int[n];
    for (i = 0; i < n; i++)
    {
        std::cin >> p[i];
    }
    for (i = 0; i < n; i++)
    {

        if (p[i] >= p[k - 1] && p[i] > 0)
        {
            c += 1;
        }
    }
    delete[] p;
    std::cout << c << std::endl;
    return 0;
}