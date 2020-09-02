from BaseTriangle import Triangle


def test_isTriangleDifferentQuaters():
    tr = Triangle((1, 10), (-4, -6), (-5, 3))
    assert tr.isTriangle()

def test_isTriangleEgyptTriangle():
    tr = Triangle((0, 0), (0, 3), (4, 0))
    assert tr.isTriangle()

def test_isTriangleisEdgeParallelOY():
    tr = Triangle((1, 10), (0, 12), (1, 5))
    assert tr.isTriangle()


def test_isTriangleIsEdgeParallelOX():
    tr = Triangle((7, 5), (10, 5), (8.5, 1))
    assert tr.isTriangle()


def test_isTriangleisVertexesOnLine():
    tr = Triangle((1, 17), (2.5, 23), (-3, 1))
    assert not tr.isTriangle()

