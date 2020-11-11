import math

# Two dimensional rotation
# returns coordinates in a tuple (x,y)
def rotate(x, y, r):
    rx = (x*math.cos(r)) - (y*math.sin(r))
    ry = (y*math.cos(r)) + (x*math.sin(r))
    return (rx, ry)

# create a ring of points centered on center (x,y) with a given radius
# using the specified number of points
# center should be a tuple or list of coordinates (x,y)
# returns a list of point coordinates in tuples
# ie. [(x1,y1),(x2,y2
def point_ring(center, num_points, radius):
    arc = (2 * math.pi) / num_points # what is the angle between two of the points
    points = []
    for p in range(num_points):
        (px,py) = rotate(0, radius, arc * p)
        px += center[0]
        py += center[1]
        points.append((int(px),int(py)))
    return points

x = 0
y = 0
my_points = {"x": [], "y": []}

# loop through the points created from a ring centered at (150,150),
# with a radius of 10, using 96 points
# and insert them into our shape file as features


for point in point_ring((500,500),3000, 300):
   x,y = point
   my_points['x'].append(x)
   my_points['y'].append(y)

print(my_points)