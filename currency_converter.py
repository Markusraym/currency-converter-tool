import requests

def get_rates(api_key, currencies):
    #Join the currencies to a string separated by commas, which is the format required by the API
    symbols = ','.join(currencies)
    
    #URL to match the provided endpoint
    url = f'http://api.exchangeratesapi.io/v1/latest?access_key={api_key}&symbols={symbols}'
     
    #Send a request to the API service.
    response = requests.get(url)
    
    #Parse the response as JSON to get a dictionary.
    data = response.json()
    
    #Check if the 'rates' key is in the response before proceeding
    if 'rates' not in data:
        print("Error retrieving data from the API.")
        print(data)  #Print the error message from the API
        return None
    
    #Return the dictionary of rates.
    return data['rates']

def convert(amount, src, dest, rates):
    #Handle the case where the source or destination currency is EUR
    src_rate = rates[src] if src != 'EUR' else 1
    dest_rate = rates[dest] if dest != 'EUR' else 1
    
    #Calculate the converted amount
    return amount * dest_rate / src_rate


#  actual key received from the API service.
api_key = '0f9d80a1cb76e55288c0a2a158d7d510' 

# List of currencies you want to get rates for, excluding the base currency (EUR).
currencies = ['USD', 'GBP'] # EUR is excluded because it's the default base currency

# Call the get_rates function with the API key and list of currencies.
rates = get_rates(api_key, currencies)

if rates is not None:
    # Get user input for the amount and currencies to convert from and to.
    amount = float(input("Enter the amount to convert: "))
    src = input("Enter source currency (USD, EUR, GBP): ")
    dest = input("Enter destination currency (USD, EUR, GBP): ")

    # If the source currency is EUR, we don't need to convert it.
    if src != 'EUR':
        amount = convert(amount, 'EUR', src, rates)
    
    # Perform the conversion.
    converted_amount = convert(amount, src, dest, rates)

    # Print out the converted amount.
    print(f"{amount} {src} is {converted_amount:.2f} {dest}")
else:
    print("Could not retrieve rates to perform the conversion.")
