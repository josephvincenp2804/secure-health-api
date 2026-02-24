def test_minimize():
<<<<<<< HEAD
    from app.compliance import data_minimize
=======
    from compliance import data_minimize
>>>>>>> a0036b4867e917ca07ce2b1c346e6c23f8d75649
    p = {'id':'1','name':'A','dob':'2000-01-01','consent':True,'ssn':'X'}
    m = data_minimize(p)
    assert 'ssn' not in m and 'name' in m