#include <iostream>
#include <cmath>
struct point
{
    int x;
    int y;
};
int main()
{
    int i, j, distance;
    int matrix[5][5];
    point middlePoint = {2, 2};
    point initPoint;
    point diffPoint;

    for (i = 0; i < 5; i++)
    {
        for (j = 0; j < 5; j++)
        {

            std::cin >> matrix[i][j];
            if (matrix[i][j] == 1)
            {
                initPoint.x = i;
                initPoint.y = j;
            }
        }
    }

    diffPoint.x = abs(initPoint.x - middlePoint.x);
    diffPoint.y = abs(initPoint.y - middlePoint.y);
    distance = diffPoint.x + diffPoint.y;

    std::cout << distance << std::endl;

    return 0;
}