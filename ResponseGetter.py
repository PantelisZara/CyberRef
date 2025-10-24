import requests
import base64

def urlChecker(url : str, ApiKey : str):
    
    
    encoded_url = base64.urlsafe_b64encode(url.encode()).decode().strip("=")    # Converts user's input to a virus_total compatible URL

    response = requests.get(f"https://www.virustotal.com/api/v3/urls/{encoded_url}", headers={"x-apikey": ApiKey})   

    if response.status_code != 200:   
        print(f"Error: {response.status_code} / {response.text}")
        return

    data = response.json()
    attributes = data.get("data", {}).get("attributes", {})
    
    
    stats = attributes.get("last_analysis_stats", {})
    trackers = attributes.get("trackers", [])
    outgoing_links = attributes.get("outgoing_links", [])  
    votes = attributes.get("total_votes", {})

    return (stats, trackers, outgoing_links, votes)
