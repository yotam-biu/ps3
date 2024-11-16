from edge_case_exercise import move

def test_edge_case():
    print("start the test!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    assert move([0,0,0,1,0,0,0], "left") ==  [0,0,1,0,0,0,0]
