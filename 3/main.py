def main():
    with open('input') as f:
        wires = [(line.rstrip('\n')).split(',') for line in f]

    grid = [{},{}]
    idx = 0 

    for directions in wires:
        steps = 0
        directions = wires[idx]
        x, y = 0,0
        for direction in directions:
            if direction[0] == 'R':
                addx, addy = 1, 0
            elif direction[0] == 'L':
                addx, addy = -1, 0
            elif direction[0] == 'U':
                addx, addy = 0, 1
            elif direction[0] == 'D':
                addx, addy = 0, -1
            
            for i in range(int(direction[1:])):
                x += addx
                y += addy 
                steps += 1

                if (x,y) not in grid[idx]:
                    grid[idx][(x,y)] = steps 
        idx += 1
    #Convert dict keys into sets then and them
    intersect = set(grid[0]) & set(grid[1])
    part1 = min([abs(points[0]) + abs(points[1]) for  points in intersect])
    part2 = min([grid[0][point] + grid[1][point] for point in intersect])
    
    print("Part 1: " + str(part1))
    print("Part 2: " + str(part2))

if __name__ == "__main__":
    main()
