# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access items
print(band["vocals"])
print(band.get("guitar"))

# list all the keys
print(band.keys())

# list all values
print(band.values())

# list all keys and values
print(band.items())
      
      
      
      
      
      
      
      
# Delete and clear
band["drums"] = "Bonham"
del band["drums"]    
print(band)

band2.clear()
print(band2)

del band2      
      
      
      
# Copy distionaries




      