#include <iostream>
#include <string>

int main()
{
    int n, i;
    std::string *p;
    std::cin >> n;
    p = new std::string[n];
    if (n >= 1 && n <= 100)
    {
        for (i = 0; i < n; i++)
        {
            std::cin >> p[i];
        }
        for (i = 0; i < n; i++)
        {
            if (p[i].length() > 10)
            {
                std::cout << p[i].front() << p[i].length() - 2 << p[i].back() << std::endl;
            }
            else
            {
                std::cout << p[i] << std::endl;
            }
        }
    }

    delete[] p;
    return 0;
}