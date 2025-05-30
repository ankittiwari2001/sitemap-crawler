Perfect! Here's a complete and polished version of your `README.md` with both tools (`index.py` and `merge_json.py`) documented clearly under one project:

---

### 📄 `README.md`

````markdown
# 🕷️ sitemap-crawler

A simple interactive Python script to crawl sitemap XML files and extract URLs.

---

## 🔧 Features

- Fetches and lists all nested sitemap files from a given sitemap index.
- Allows you to select which sitemap to extract from.
- Lets you choose how many URLs to extract (or extract all).
- Saves the extracted URLs into a `JSON` file.

---

## 🚀 Usage: `index.py`

### 1. Run the crawler:

```bash
python index.py
````

### 2. Example workflow:

```
Enter the base sitemap URL: https://www.mohawkgeneralstore.com
5 sitemap(s) found:
1. https://www.mohawkgeneralstore.com/sitemap_products_1.xml
2. ...
Which sitemap do you want to extract from? (1 to 5): 1
Found 2000 URLs.
How many URLs do you want to extract? (Press Enter for all): 150

Saved 150 URLs to 'extracted_urls.json'.
```

### 📂 Output:

```bash
extracted_urls.json
```

---

## 🛠 Utility: `merge_json.py`

This script merges all `.json` files in a given directory into one file.

### 📌 Features

* Accepts a directory path containing multiple `.json` files.
* Merges them into a single output file `merged_output.json`.
* Handles both list-style and object-style JSON.

### ▶️ Run the script:

```bash
python merge_json.py
```

You'll be prompted for a directory path.

---

## 📦 Dependencies

* Python 3.6+
* [`requests`](https://pypi.org/project/requests/)

Install with:

```bash
pip install -r requirements.txt
```

(Dependency management will be modularized in future versions.)

---

## 📝 License

MIT License

```

---

Let me know if you'd like a `requirements.txt`, GitHub repo setup help, or to automate the merging script with command-line arguments.
```
s