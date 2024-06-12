def solve_quadratic(a, b, c):
    # Discriminant
    discriminant = b ** 2 - 4 * a * c

    # Roots
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)

    return x1, x2
