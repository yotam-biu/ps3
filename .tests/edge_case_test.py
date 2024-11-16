from edge_case_exercise import move

def test_edge_case():
    assert move([0, 1, 0], "left") == [1, 0, 0], "Test failed: move([0, 1, 0], 'left') should return [1, 0, 0]."
    assert move([0, 1, 0], "right") == [0, 0, 1], "Test failed: move([0, 1, 0], 'right') should return [0, 0, 1]."
    assert move([1, 0], "left") == [1, 0], "Test failed: move([1, 0], 'left') should return [1, 0]."
    assert move([0, 1], "left") == [1, 0], "Test failed: move([0, 1], 'left') should return [1, 0]."
    assert move([1, 0], "right") == [0, 1], "Test failed: move([1, 0], 'right') should return [0, 1]."
    assert move([0, 1], "right") == [0, 1], "Test failed: move([0, 1], 'right') should return [0, 1]."
    assert move([1], "right") == [1], "Test failed: move([1], 'right') should return [1]."
    assert move([1], "left") == [1], "Test failed: move([1], 'left') should return [1]."
    assert move([0, 0, 0, 1, 0, 0, 0], "left") == [0, 0, 1, 0, 0, 0, 0], "Test failed: move([0, 0, 0, 1, 0, 0, 0], 'left') should return [0, 0, 1, 0, 0, 0, 0]."
    assert move([1, 0, 0, 0, 0, 0, 0], "right") == [0, 1, 0, 0, 0, 0, 0]
    assert move([1, 0, 0, 0, 0, 0, 0], "left") == [1, 0, 0, 0, 0, 0, 0]
    assert move([0, 0, 0, 0, 0, 0, 1], "left") == [0, 0, 0, 0, 0, 1, 0]
    assert move([0, 0, 0, 0, 0, 0, 1], "right") == [0, 0, 0, 0, 0, 0, 1]

