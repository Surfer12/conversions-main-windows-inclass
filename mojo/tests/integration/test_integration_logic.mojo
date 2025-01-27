fn test_decimal_to_binary_integration():
    assert decimal_to_binary(-123) == "11111111111111111111111110000101"
    assert decimal_to_binary(123) == "1111011"

fn test_binary_to_decimal_integration():
    assert binary_to_decimal("11111111111111111111111110000101") == -123
    assert binary_to_decimal("00000000000000000000000001111011") == 123 