def number_to_words(n):
    # Words for thousand, million, billion
    thousands = ['', 'Thousand', 'Million', 'Billion']
    
    # Words for multiples of ten
    tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

    # Words for numbers less than 20
    under_20 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 
                'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    
    
    

    # function to convert numbers less than 1000
    def convert_below_1000(num):
        if num < 20:
            return under_20[num]  # Directly use the word from under_20 list
        elif num < 100:
            return tens[num // 10] + ('' if num % 10 == 0 else ' ' + under_20[num % 10])  # Tens + ones
        else:
            return under_20[num // 100] + ' Hundred' + ('' if num % 100 == 0 else ' ' + convert_below_1000(num % 100))  # Hundreds + remainder

    # return zero if 0 
    if n == 0:
        return 'Zero'
    
    # Initialize result string
    result = ''
    unit = 0  # Keeps track of thousand, million, billion

    # Loop through the number in chunks of 1000
    while n > 0:
        chunk = n % 1000  # Get the last three digits
        if chunk != 0:
            result = convert_below_1000(chunk) + ' ' + thousands[unit] + ' ' + result  # Convert the chunk and add the unit
        n //= 1000  # Remove the last three digits
        unit += 1  # Move to the next unit (thousand, million, etc.)

    return result.strip()  # Return the final result without extra spaces

# Example usage
number = 11523523
print(f"{number} in words is: {number_to_words(number)}")
