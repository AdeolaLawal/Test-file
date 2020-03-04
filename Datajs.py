import json
data = """
{
    "states": [
    
        {
            "name": "Alabama",
            "abbreviation": "AL",
            "area_codes": ["20", "34","38"]
        },
        
        {
            "name": "Alaska",
            "abbreviation": "Ak",
            "area_codes": ["201", "342","386"]
        },
        
        {
            "name": "Arizona",
            "abbreviation": "AZ",
            "area_codes": ["206", "344","380"]
        },
        
        {
            "name": "Arkansas",
            "abbreviation": "AR",
            "area_codes": ["420", "834","538"]
        }
        
    ]
}
"""
json_data = json.loads(data)
print(data)