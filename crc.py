def xor(a, b):
    result = []
    for i in range(len(b)):  # Use the length of b, as that's the smaller string in division steps
        result.append('0' if a[i] == b[i] else '1')
    return ''.join(result)

def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[:pick]  # Initial pick length of divisor
    
    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0' * len(divisor), tmp) + dividend[pick]
        pick += 1
        tmp = tmp.lstrip('0')  # Strip leading zeros to maintain correct lengths
        
    # Final XOR step after loop
    if len(tmp) >= len(divisor) and tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * len(divisor), tmp)
        
    return tmp.lstrip('0')  # Return the remainder without leading zeros

def encode_data(data, key):
    l_key = len(key)
    appended_data = data + '0' * (l_key - 1)  # Append zeros for division
    remainder = mod2div(appended_data, key)
    final_data = data + remainder  # Encoded data
    return final_data, remainder

data = "101010"  # Example data
key = "1101"     # Example key
encoded_data, remainder = encode_data(data, key)

print("Original data:", data)
print("Remainder:", remainder)
print("Final data to be sent:", encoded_data)
