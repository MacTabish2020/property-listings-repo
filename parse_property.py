from bs4 import BeautifulSoup
import json
import pandas as pd

with open("/Users/tabishbaig/Documents/Scraping Projects/99acresScraper/99acres_listings.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

script_tags = soup.find_all("script", {"type": "application/ld+json"})

properties = []
print(f"Total script tags found: {len(script_tags)}")
for tag in script_tags:
    try:
        data = json.loads(tag.text)
        print("Found type:", data.get("@type"))
        if data.get("@type") == "Apartment":
            print("Adding apartment:", data.get("name"))
            property_info = {
                "Project Name": data.get("address", {}).get("name"),
                "Title": data.get("name"),
                "Description": data.get("description"),
                "Number of Rooms": data.get("numberOfRooms").strip() if data.get("numberOfRooms") else None,
                "Bathrooms": data.get("numberOfBathroomsTotal"),
                "Floor Size": data.get("floorSize"),
                "Floor Level": data.get("floorlevel"),
                "Link": data.get("url"),
                "Street Address": data.get("address", {}).get("streetAddress"),
                "Locality": data.get("address", {}).get("addressLocality"),
                "Latitude": str(data.get("geo", {}).get("latitude")),
                "Longitude": str(data.get("geo", {}).get("longitude"))
            }
            properties.append(property_info)
    except Exception as e:
        print("Error parsing tag:", e)
        continue

# Convert list of dictionaries to DataFrame
df = pd.DataFrame(properties)

# Save to CSV
df.to_csv("property_listings.csv", index=False)
