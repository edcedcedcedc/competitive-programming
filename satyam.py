
for _ in range(int(input())):
    points = int(input())
    result = 0
    coordinates = []
    count_x = {}

    for _ in range(points):
        x,y = input().split()
        coordinates.append((int(x),int(y)))
    
    for i in range(len(coordinates)):
        if coordinates[i][0] not in count_x:
            count_x[coordinates[i][0]] = 1
        else:
            count_x[coordinates[i][0]] += 1

    """ With the rest of the 
        angles form a non-degenerate triangles
        y1--x--x1--x2--xn-----
            
        y---x----x2-------

        Pyt identity 
        a^2 + b^2 = c^2
        """
    for i in count_x:
        if count_x[i] == 2: 
            result += points - 2

    uniq_coordinates = set(coordinates)
    """
    Form a non-degenerate triangle
    y1----x-------

    y--x-1-x+1-------
     """
    for x,y in uniq_coordinates:
        if (((x - 1, 0 if y == 1 else 1) in uniq_coordinates) and 
            ((x + 1, 0 if y == 1 else 1) in uniq_coordinates)): 
            result += 1
            
    print(result)

