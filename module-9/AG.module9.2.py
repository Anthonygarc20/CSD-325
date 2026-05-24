"""
Author: Garcia Anthony
Assignment: Module 9.2 - Task 2 (Custom Simple API)
Description: A standalone program that connects to a simple API, 
             tests the connection, prints unformatted response data, 
             and prints formatted output matching the tutorial style.
"""

import requests

def main():
    # 6.a. Find a simple API. 
    # (Using a reliable, free random jokes API that requires no authentication)
    url = 'https://official-joke-api.appspot.com/random_joke'
    
    # 6.b. Test the connection to your API, output results.
    print("--- 6.b. Testing Connection to Custom API ---")
    response = requests.get(url)
    print(f"Status Code: {response.status_code}\n")
    
    # Proceed if the connection is successful (Status Code 200)
    if response.status_code == 200:
        data = response.json()
        
        # 6.c. Print out the response from the request, with no formatting.
        print("--- 6.c. Raw Response From Request (No Formatting) ---")
        print(data)
        print("\n")
        
        # 6.d. Print out the response with same formatting as the tutorial program.
        print("--- 6.d. Formatted Response ---")
        print(f"Setup    : {data.get('setup')}")
        print("-" * 50)
        print(f"Punchline: {data.get('punchline')}")
        print(f"ID       : {data.get('id')}")
        print(f"Type     : {data.get('type')}")
        
    else:
        print(f"Connection failed. Unable to fetch data. Status: {response.status_code}")

if __name__ == "__main__":
    main()