from cs1graphics import *

# Pixels per grid-cell
size = float(input('Enter a number of pixels per grid-cell: '))

paper = Canvas(15 * size, 13 * size)
paper.setBackgroundColor('burlywood4')

# Adding numbers on the board

for num in range(24):
    numBoard = Text()
    numBoard.setMessage(str(num + 1))
    
    # Moving the numbers at specific positions
    if num <= 11:
        x = ((1.5 + num // 6)   * size) + (size * num)
        y = 12.5 * size 
    else:
        x = ((13.5 - num // 18) * size) - (size * (num % 12))
        y = 0.5 * size
    
    numBoard.moveTo(x, y)
    paper.add(numBoard)

# Adding the background rectangles

for k in range(2):
    backRect = Rectangle(6*size, 11*size)
    backRect.setFillColor('navajowhite')
    backRect.moveTo( 4 * size + ((k * 7) * size), 6.5 * size)
    paper.add(backRect)

# Adding the middle line

line = Path(Point(7.5 * size, 0), Point(7.5 * size, 13 * size))
paper.add(line)

# Adding the triangles

for k in range(2):
    
    # Adding the bottom triangles
    if k == 0:
        triLayer = Layer()
        triLayer.moveTo(7.5 * size, 12 * size)
        for k in range(12):
            tri = Polygon(Point(6*size, -5*size), Point(5.5*size, 0), Point(6.5*size, 0))
            tri.setFillColor("tan" if k % 2 == 0 else "darkorange3")
            # Specifying the x-position depending on the index
            if k <= 5:
                x = -k * size
            else:
                x = (-k-1) * size
            # Moving to a specific position
            tri.move(x, 0)
            triLayer.add(tri)
        paper.add(triLayer)
    
    # Adding the top triangles
    else:
        triTop = triLayer.clone()
        triTop.flip(90)
        triTop.flip()
        triTop.move(0, -11*size)
        paper.add(triTop)

# Adding the circles

for num,pt,whiteOnTop in [(2,1,True), (5,6,False), (3,9,False), (5,13,True)]:

    for k in range(num):
        # Adding the bottom checkers
        checker = Circle(0.45*size)
        checker.moveTo(size*(pt+0.5), (11.55-k*0.9)*size)
        checker.setFillColor('Black' if whiteOnTop else 'White')
        paper.add(checker)
        
        # Adding the top checkers
        checkerTop = checker.clone()
        checkerTop.moveTo(size*(pt+0.5), (1.45+k*0.9)*size)
        checkerTop.setFillColor('White' if whiteOnTop else 'Black')
        paper.add(checkerTop)
        