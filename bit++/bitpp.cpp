#include <iostream>
#include <string>
int main()
{
    int x = 0, i, n;
    const std::string ppX = "++X";
    const std::string Xpp = "X++";
    std::cin >> n;
    std::string *p = new std::string[n];

    for (i = 0; i < n; i++)
    {
        std::cin >> p[i];
        if (p[i] == ppX || p[i] == Xpp)
        {
            x += 1;
        }
        else
        {
            x -= 1;
        }
    }
    std::cout << x << std::endl;
    delete[] p;
    return 0;
}