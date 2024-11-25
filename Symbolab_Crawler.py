import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


CHROMEDRIVER_PATH = "/usr/local/bin/chromedriver/chromedriver"

def setup_driver():
    """Sets up the Chrome WebDriver."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    service = Service(CHROMEDRIVER_PATH)
    return webdriver.Chrome(service=service, options=options)


# Utility functions
def clean_formula_text(raw_text):
    """Cleans and formats the formula text."""
    parts = raw_text.split()
    cleaned_parts = [part for part in parts if not part.replace(".", "").isnumeric()]
    cleaned_text = " ".join(cleaned_parts).replace("∫∫", "∫").replace("d dx", "d/dx").strip()
    cleaned_text = cleaned_text.replace("\u03c0", "pi").replace("( )", "()")
    return cleaned_text


# Scraping functions
def scrape_page(driver, url, difficulty, category):
    """Scrapes a single page for formulas."""
    try:
        driver.get(url)
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll to load more
        time.sleep(2)

        problems = []
        formula_elements = driver.find_elements(By.CLASS_NAME, "mathquill-rendered-math")
        for element in formula_elements:
            try:
                raw_text = element.text.strip()
                cleaned_text = clean_formula_text(raw_text)
                if cleaned_text:
                    problems.append({"difficulty": difficulty, "category": category, "question": cleaned_text})
            except Exception as e:
                problems.append({"difficulty": difficulty, "category": category, "error": str(e)})

        print(f"Scraped {len(problems)} problems from {category} ({difficulty}) page.")
        return problems

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []


def scrape_all_pages(driver, subpages):
    """Scrapes all pages based on provided subpages."""
    all_problems = []
    for url, info in subpages.items():
        print(f"Scraping {info['category']} ({info['difficulty']}) from {url}")
        problems = scrape_page(driver, url, info["difficulty"], info["category"])
        all_problems.extend(problems)
    return all_problems


def save_to_json(data, filename):
    """Saves scraped data to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filename}")


if __name__ == "__main__":
    subpages = {
        "https://www.symbolab.com/worksheets/Calculus/Integrals_New/Basic": {"difficulty": "Basic", "category": "Constant Rule"},
        "https://www.symbolab.com/worksheets/Calculus/Integrals_New/Moderate": {"difficulty": "Moderate", "category": "Power Rule"},
        "https://www.symbolab.com/worksheets/Calculus/Integrals_New/Advanced": {"difficulty": "Advanced", "category": "Integration by Parts"},
        "https://www.symbolab.com/worksheets/Calculus/Multiple-Integrals": {"difficulty": "Advanced", "category": "Multiple Integrals"},
    }

    driver = setup_driver()
    try:
        all_problems = scrape_all_pages(driver, subpages)
        save_to_json(all_problems, "integral_problems.json")
    finally:
        driver.quit()
