import requests
import xml.etree.ElementTree as ET
import json

def fetch_xml(url):
    try:
        print(f"Fetching: {url}")
        response = requests.get(url)
        response.raise_for_status()
        return ET.fromstring(response.content)
    except Exception as e:
        print(f"Error fetching/parsing URL: {url}\n{e}")
        return None

def extract_sitemap_links(base_url):
    root = fetch_xml(base_url)
    if root is None:
        return []

    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    sitemap_tags = root.findall("ns:sitemap", namespace)
    sitemap_urls = [tag.find("ns:loc", namespace).text for tag in sitemap_tags if tag.find("ns:loc", namespace) is not None]
    
    return sitemap_urls

def extract_urls_from_sitemap(sitemap_url, limit=None):
    root = fetch_xml(sitemap_url)
    if root is None:
        return []

    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    url_tags = root.findall("ns:url", namespace)
    urls = [tag.find("ns:loc", namespace).text for tag in url_tags if tag.find("ns:loc", namespace) is not None]

    return urls[:limit] if limit else urls

def main():
    base_url = input("Enter the base sitemap URL: ").strip()
    sitemap_urls = extract_sitemap_links(base_url)

    if not sitemap_urls:
        print("No sitemaps found.")
        return

    print(f"\n{sitemap_urls.__len__()} sitemap(s) found:")
    for i, url in enumerate(sitemap_urls, 1):
        print(f"{i}. {url}")

    index_input = input(f"\nWhich sitemap do you want to extract from? (1 to {len(sitemap_urls)}): ").strip()
    if not index_input.isdigit() or not (1 <= int(index_input) <= len(sitemap_urls)):
        print("Invalid input. Exiting.")
        return

    selected_sitemap = sitemap_urls[int(index_input) - 1]

    all_urls = extract_urls_from_sitemap(selected_sitemap)
    if not all_urls:
        print("No URLs found in selected sitemap.")
        return

    print(f"\n{len(all_urls)} URLs found in the selected sitemap.")
    limit_input = input("How many URLs do you want to extract? (Press Enter for all): ").strip()
    limit = int(limit_input) if limit_input.isdigit() else None
    selected_urls = all_urls[:limit] if limit else all_urls

    # Save to JSON
    output_file = "extracted_urls.json"
    with open(output_file, "w") as f:
        json.dump(selected_urls, f, indent=2)

    print(f"\nSaved {len(selected_urls)} URLs to '{output_file}'.")

if __name__ == "__main__":
    main()
