# HTTP Response Code Check
response_code = int(input("Enter HTTP response code: "))

if response_code >= 200 and response_code < 300:
    print("Success")
elif response_code >= 300 and response_code < 400:
    print("Redirect")
elif response_code >= 400 and response_code < 404:  
    print("Client error")
elif response_code == 404:
    print("Client error: Not Found")
elif response_code >= 405 and response_code < 500:
    print("Client error")
elif response_code == 500:
    print("Server error: Internal Server Error")
elif response_code > 500 and response_code < 600:
    print("Server error")
else:
    print("Invalid Status Code")