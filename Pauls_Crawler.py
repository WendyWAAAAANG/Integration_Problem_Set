import random
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


def setup_driver():
    """Sets up and returns a Chrome WebDriver instance."""
    options = Options()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


def scrape_mathjax_problems(driver, url, category, difficulty="Moderate"):
    """Scrapes problems rendered with MathJax from a given URL."""
    driver.get(url)
    
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "script"))
        )
    except TimeoutException:
        print("Timeout: MathJax content did not load in time.")
        return []

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    problems = []

    mathjax_scripts = soup.find_all("script", {"type": "math/tex"})
    if not mathjax_scripts:
        print(f"No MathJax <script> tags found on the page: {url}")
        return []

    for script in mathjax_scripts:
        try:
            problem_text = script.text.strip()
            if not problem_text:
                continue

            problems.append({
                "difficulty": random.choice(["Basic", "Moderate", "Advanced"]) if difficulty == "Mixed" else difficulty,
                "category": category,
                "question": problem_text
            })
        except Exception as e:
            print(f"Error processing a MathJax problem: {e}")
            continue

    print(f"Scraped {len(problems)} problems from {category} page.")
    return problems


def save_to_json(data, filename):
    """Saves scraped data to a JSON file."""
    with open(filename, 'w', encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=True)
    print(f"Data saved to {filename}")


def main():
    driver = setup_driver()

    # URLs and categories to scrape
    urls_to_scrape = [
        {"url": "https://tutorial.math.lamar.edu/ProblemsNS/CalcII/PartialFractions.aspx", "category": "Partial Fractions", "difficulty": "Moderate"},
        {"url": "https://tutorial.math.lamar.edu/ProblemsNS/CalcII/ImproperIntegrals.aspx", "category": "Improper Integrals", "difficulty": "Advanced"},
        {"url": "https://tutorial.math.lamar.edu/ProblemsNS/CalcII/IntegralsWithTrig.aspx", "category": "Trigonometric Substitution", "difficulty": "Mixed"},
        {"url": "https://tutorial.math.lamar.edu/ProblemsNS/CalcII/IntegrationByParts.aspx", "category": "Integration by Parts", "difficulty": "Mixed"},
        {"url": "https://tutorial.math.lamar.edu/ProblemsNS/CalcII/TrigSubstitutions.aspx", "category": "Trigonometric Substitution", "difficulty": "Mixed"},
    ]

    all_problems = []

    try:
        for item in urls_to_scrape:
            print(f"Scraping: {item['url']} (Category: {item['category']})")
            problems = scrape_mathjax_problems(driver, item['url'], item['category'], item['difficulty'])
            all_problems.extend(problems)

        if all_problems:
            save_to_json(all_problems, "mathjax_problems.json")
            print("Extraction complete!")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
