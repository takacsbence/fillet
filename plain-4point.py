import numpy as np

def plane_from_points(p1, p2, p3, p4):
    # Convert to numpy arrays
    p1, p2, p3, p4 = map(np.array, (p1, p2, p3, p4))
    
    # Create vectors in the plane
    v1 = p2 - p1
    v2 = p3 - p1
    
    # Compute normal vector using cross product
    normal = np.cross(v1, v2)
    
    if np.linalg.norm(normal) == 0:
        raise ValueError("The first three points are collinear and do not define a plane.")
    
    # Plane equation: Ax + By + Cz + D = 0
    A, B, C = normal
    D = -np.dot(normal, p1)
    
    # Check coplanarity of the fourth point
    coplanarity_check = A * p4[0] + B * p4[1] + C * p4[2] + D
    if not np.isclose(coplanarity_check, 0, atol=1e-6):
        raise ValueError("The four points are not coplanar, so a single plane cannot be defined.")
    
    return A, B, C, D
