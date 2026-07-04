# Read an integer N from standard input: the number of points.
# N satisfies 3 <= N <= 10^5, so we should use O(N) time and avoid quadratic algorithms.
N = int(input())

# Initialize min and max trackers for x and y.
# We set minx and miny to values larger than any possible coordinate (coordinates <= 1000),
# so the first point will correctly lower them.
minx = 1001
miny = 1001

# We set maxx and maxy to values smaller than any possible coordinate (coordinates >= 0),
# so the first point will correctly raise them.
maxx = -1
maxy = -1

# Loop over each of the N input points.
# For each point we parse two integers tempx and tempy from input.
# We update the running min and max for x and y in O(1) time per point.
for i in range(N):
    # Read one line containing two integers and unpack into tempx and tempy.
    tempx, tempy = map(int, input().split())

    # Update the maximum x seen so far.
    # If tempx is greater than the current maxx, replace maxx with tempx.
    maxx = max(maxx, tempx)

    # Update the maximum y seen so far.
    # If tempy is greater than the current maxy, replace maxy with tempy.
    maxy = max(maxy, tempy)

    # Update the minimum x seen so far.
    # If tempx is smaller than the current minx, replace minx with tempx.
    minx = min(minx, tempx)

    # Update the minimum y seen so far.
    # If tempy is smaller than the current miny, replace miny with tempy.
    miny = min(miny, tempy)

# After processing all points:
# width is the difference between the largest and smallest x coordinates.
# height is the difference between the largest and smallest y coordinates.
# The area of the smallest axis-aligned rectangle containing all points is width * height.
# A point may lie on the boundary of the box; that is allowed by the problem statement.
area = (maxy - miny) * (maxx - minx)

# Print the computed area as a single integer on one line.
print(area)
