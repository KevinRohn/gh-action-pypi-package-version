import sys
import requests
from typing import Tuple, Dict, Any
import json

def get_package_info(repo: str, package: str) -> Tuple[str, Dict[str, Any]]:
    base_urls = {
        'pypi': 'https://pypi.org',
        'testpypi': 'https://test.pypi.org'
    }
    
    if repo not in base_urls:
        raise ValueError("Repository must be either 'pypi' or 'testpypi'")
        
    url = f"{base_urls[repo]}/pypi/{package}/json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    latest_version = data['info'].get('version')
    if not latest_version:
        # If no version in info, get latest from releases
        versions = sorted(data['releases'].keys(), 
                        key=lambda x: [int(i) for i in x.split('.')])
        latest_version = versions[-1] if versions else "No version found"
    
    return latest_version, data['releases']

def main():
    if len(sys.argv) != 3:
        print("Usage: script.py <pypi|testpypi> <package-name>")
        sys.exit(1)
        
    repo, package = sys.argv[1], sys.argv[2]
    
    try:
        latest_version, releases = get_package_info(repo, package)
        output = {
            "latest_version": latest_version,
            "all_releases": list(releases.keys())
        }
        print(json.dumps(output, indent=2))
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()