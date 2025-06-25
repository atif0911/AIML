# #key and value 
# like jan->january, first month of year
# feb-> ...

monthConversion ={ #keys can be any data type
    "jan":"January",
    "feb":"February",
    "mar":"March",
    "apr":"April"
}

print(monthConversion["jan"])
print(monthConversion.get("feb"))
print(monthConversion.get("dec")) #since not present shows none
print(monthConversion.get("dec","Not a valid key")) #since not present we set a default value