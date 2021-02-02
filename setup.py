"""arquivo necessario para tornar o pacote instalavel."""
from setuptools import setup, find_packages

setup(
    name="git-scraping",
    version="0.1.0",
    description="List all files in a github repository and save in txt",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["httpx", "beautifulsoup4"],
    test_suite='test',
)
