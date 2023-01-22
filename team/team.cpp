#include <iostream>

int main()
{
    const int TEAM = 3;
    bool solution[3];
    int problems, track = 0, implement = 0;

    std::cin >> problems;
    for (int i = 0; i < problems; i++)
    {
        for (int j = 0; j < TEAM; j++)
        {
            std::cin >> solution[j];
            if (solution[j] == true)
            {
                track++;
                if (track >= 2)
                {
                    implement++;
                    track = 0;
                }
            }
        }
        track = 0;
    }
    std::cout << implement << std::endl;
    return 0;
}