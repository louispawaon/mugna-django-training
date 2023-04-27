from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def math_view(request, num1, num2, num3=None):
    # Parse the parameters as integers
    numbers = [int(num1), int(num2)]
    if num3:
        numbers.append(int(num3))

    # Compute the results
    total_sum = sum(numbers)
    difference = numbers[0] - numbers[1]
    product = numbers[0] * numbers[1]
    quotient = numbers[0] / numbers[1]

    # Build the response
    response = f"Sum: {total_sum}\nDifference: {difference}\nProduct: {product}\nQuotient: {quotient}"
    return HttpResponse(response)

def valid_date_view(request, YYYY, MM, DD):
    try:
        # Try to create a date object with the provided parameters
        from datetime import datetime
        datetime(int(YYYY), int(MM), int(DD))
        response = "Valid date"
    except ValueError:
        response = "Invalid date"

    # Build the response
    return HttpResponse(response)