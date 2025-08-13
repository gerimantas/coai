"""
Web API client with authentication and error handling issues
"""

import requests
import time
from typing import Dict, List, Optional

class APIClient:
    def __init__(self, base_url: str, api_key: str = None):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.session = requests.Session()
        if api_key:
            self.session.headers.update({'Authorization': f'Bearer {api_key}'})
    
    def get(self, endpoint: str, params: Dict = None):
        # Missing comprehensive error handling
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.get(url, params=params)
        return response.json()  # Will crash if response is not JSON
    
    def post(self, endpoint: str, data: Dict):
        # No retry logic for failed requests
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.post(url, json=data)
        if response.status_code != 200:
            raise Exception(f"Request failed: {response.status_code}")
        return response.json()
    
    def batch_requests(self, endpoints: List[str]):
        # Inefficient - should use async or threading
        results = []
        for endpoint in endpoints:
            result = self.get(endpoint)
            results.append(result)
            time.sleep(0.1)  # Rate limiting - but not configurable
        return results
    
    def upload_file(self, endpoint: str, file_path: str):
        # Missing file validation and error handling
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        with open(file_path, 'rb') as f:  # Will crash if file doesn't exist
            files = {'file': f}
            response = self.session.post(url, files=files)
        return response.json()
    
    def paginated_get(self, endpoint: str, page_size: int = 100):
        # Basic pagination without proper error handling
        page = 1
        all_data = []
        
        while True:
            params = {'page': page, 'size': page_size}
            data = self.get(endpoint, params)
            
            if not data:  # Assumes empty list means end of data
                break
                
            all_data.extend(data)
            page += 1
            
            if page > 1000:  # Arbitrary limit to prevent infinite loop
                break
                
        return all_data
    
    def health_check(self):
        # Basic health check without proper timeout handling
        try:
            response = self.get('/health')
            return response.get('status') == 'healthy'
        except:
            return False

# Usage example with potential issues
if __name__ == "__main__":
    # This might fail if API is down
    client = APIClient("https://jsonplaceholder.typicode.com")
    
    try:
        # This should work
        posts = client.get("/posts", {"_limit": 5})
        print(f"Retrieved {len(posts)} posts")
        
        # This might fail if endpoint doesn't exist
        users = client.get("/nonexistent")
        
    except Exception as e:
        print(f"Error: {e}")
    
    # Test health check
    print("API healthy:", client.health_check())
