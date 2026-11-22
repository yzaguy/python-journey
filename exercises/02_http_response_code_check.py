# HTTP Response Code Check
response_code = int(input("Enter HTTP response code: "))

if response_code == 404:
    print("Client error: Not Found")
elif response_code == 500:
    print("Server error: Internal Server Error")
elif response_code >= 100 and response_code <= 199:
    print("Informational response")
elif 200 <= response_code <= 299:
    print("Success")
elif 300 <= response_code <= 399:
    print("Redirect")
elif 400 <= response_code <= 499:
    print("Client error")
elif 500 <= response_code <= 599:
    print("Server error")
else:
    print("Invalid status code")