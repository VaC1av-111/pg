def prevod_C_na_F(stupne):

    return stupne * 9/5 + 32



def test_prevod_C_na_F():
    assert prevod_C_na_F(100) == 212
    assert prevod_C_na_F(0) == 32


if __name__ == "__main__":
    print(prevod_C_na_F(100))

    print (prevod_C_na_F(0))
    
    print(prevod_C_na_F(5))