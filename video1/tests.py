"""
Use this: pytest -s --capture=no tests.py
for see the result of tests
"""

from just_land import main


def test_google_title():
    title = main()
    assert "google" in title.lower()
    print("Test passed: Google title found")
