def lower_case(x):
    return x.lower()

def test_lowercase():
    """First define the given values/parameters
   when  - parameters under a certain condition
   Expectation - what am i expecting the results to be"""    
    assert lower_case('TEAM KAIZEND') == 'team kaizend'

def test_lowercase2():
    """name the function to the purporse of it"""
    assert lower_case('Team Kaizend') == 'team kaizend'

