package_name = "qaviton_log"


if __name__ == "__main__":
    from sys import version_info as v
    from setuptools import setup, find_packages
    with open("requirements.txt") as f: requirements = f.read().splitlines()
    with open("README.md", encoding="utf8") as f: long_description = f.read()
    setup(
        name=package_name,
        version="2019.11.13.14.38.8.658570",
        author="yehonadav",
        author_email="qaviton@gmail.com",
        description="qaviton log",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/qaviton/qaviton_log",
        packages=[pkg for pkg in find_packages() if pkg.startswith(package_name)],
        license="apache-2.0",
        classifiers=[
            f"Programming Language :: Python :: {v[0]}.{v[1]}",
        ],
        install_requires=requirements
    )
