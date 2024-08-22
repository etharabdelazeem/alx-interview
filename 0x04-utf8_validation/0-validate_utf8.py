def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the leading byte patterns
    mask1 = 1 << 7    # 10000000
    mask2 = 1 << 6    # 01000000

    for num in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Count the number of leading 1's
            while mask & num:
                num_bytes += 1
                mask = mask >> 1
            
            # If num_bytes is 0, it's a 1-byte character
            if num_bytes == 0:
                continue

            # UTF-8 characters can be 1 to 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the byte starts with '10'
            if not (num & mask1 and not (num & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
