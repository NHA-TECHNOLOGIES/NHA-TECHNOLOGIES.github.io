import socket



def draw_line_bresenham(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope_error_new = dy - dx

    if x1 < x2:
        step_x = 1
    else:
        step_x = -1

    if y1 < y2:
        step_y = 1
    else:
        step_y = -1

    x, y = x1, y1

    points.append((x, y))

    while x != x2 or y != y2:
        slope_error_new_2 = 2 * slope_error_new

        if slope_error_new_2 > -dx:
            slope_error_new -= dx
            y += step_y

        if slope_error_new_2 < dy:
            slope_error_new += dy
            x += step_x

        points.append((x, y))

    return points

# Line from (5, 5) to (13, 9)
line_points = draw_line_bresenham(5, 5, 13, 9)

# Print the rasterized points
for point in line_points:
    print(point)
