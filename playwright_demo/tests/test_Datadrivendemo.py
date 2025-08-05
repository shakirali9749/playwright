import re
import csv
import pytest
from playwright.sync_api import Page, expect

# Read and return all rows with line number (so we can update later)
def get_csv_data_with_index():
    data = []
    with open("test_data/data.csv", newline="") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            data.append((i, row["username"], row["password"]))
    return data

@pytest.mark.parametrize("index,username,password", get_csv_data_with_index())
def test_login(index, username, password, page: Page):
    # Open the CSV file to read existing rows
    with open("test_data/data.csv", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    try:
        # Perform login
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", timeout=60000)
        page.get_by_role("textbox", name="Username").fill(username)
        page.get_by_role("textbox", name="Password").fill(password)
        page.get_by_role("button", name="Login").click()

        # Check if dashboard appears
        expect(page).to_have_url(re.compile(r".*/dashboard/.*"), timeout=10000)
        expect(page.get_by_role("heading", name="Dashboard")).to_be_visible(timeout=10000)

        print(f"Login status for {username}/{password}: Submitted")

        # Update only the relevant row’s Status
        rows[index]["Status"] = "Submitted"

    except Exception:
        print(f"Login status for {username}/{password}: ")  # Leave status blank

    # Write updated rows back to the CSV file
    with open("test_data/data.csv", "w", newline="") as f:
        fieldnames = ["username", "password", "Status"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
