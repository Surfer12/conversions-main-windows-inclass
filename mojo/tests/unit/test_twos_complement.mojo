fn test_to_twos_complement():
    assert to_twos_complement(-123, 32) == "11111111111111111111111110000101"
    assert to_twos_complement(123, 32) == "00000000000000000000000001111011"

fn test_float_to_ieee754():
    assert float_to_ieee754(-123.456) == "c2f6c000"
    assert float_to_ieee754(123.456) == "42f6c000" 