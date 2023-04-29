from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def math_view(request, num1, num2, num3=None):
    # Parse the parameters as integers
    numbers = [int(num1), int(num2)]
    if num3:
        numbers.append(int(num3))
    else:
        numbers.append(0)

    # Compute the results
    total_sum = sum(numbers)
    difference = numbers[0] - numbers[1] - numbers[2]
    product = numbers[0] * numbers[1] * numbers [2]
    quotient = numbers[0] / numbers[1] #not sure

    context = {
        'numbers': numbers,
        'total_sum': total_sum,
        'difference': difference,
        'product': product,
        'quotient': quotient
    }

    # Build the response
    response = f"Sum: {total_sum}\nDifference: {difference}\nProduct: {product}\nQuotient: {quotient}"
    return render(request, 'math.html', context)

def valid_date_view(request, YYYY, MM, DD):
    try:
        # Try to create a date object with the provided parameters
        datetime(int(YYYY), int(MM), int(DD))
        response = "Valid date"
    except ValueError:
        response = "Invalid date"

    context = {
        'date': f"{YYYY}/{MM}/{DD}",
        'validity': response
    }

    # Build the response
    return render(request, 'valid_date.html', context)
