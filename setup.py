from setuptools import setup

with open("requirements.txt", "r", encoding="utf-8") as file:
    requirements = [
        line.strip()
        for line in file
        if line.strip() and not line.startswith("#")
    ]

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="discord-oauth2.py",
    description="Use Discord's OAuth2 effortlessly! Turns the auth code to a access token and the access token into scope infomation. ",
    version="1.2.2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    python_requires=">=3.8",
    author="Zaltro431",
    packages=["discord.py-oauth2"],
    url="https://github.com/cannies936/discord-oauth2.py",
    keywords="flask, oauth2, discord, discord-api",
    install_requires=[
        "aiohttp",
        "d",
    ],
)from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="discord-oauth2.py",
    description="Use Discord's OAuth2 effortlessly! Turns the auth code to a access token and the access token into scope infomation. ",
    version="1.2.2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    python_requires=">=3.8",
    author="Zaltro431",
    packages=["discord.py-oauth2"],
    url="https://github.com/cannies936/discord-oauth2.py",
    keywords="aiohttp, oauth2, discord, discord-api",
    install_requires=requirement
)

