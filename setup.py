"""Python setup.py for dasp_ai_agents_cowriting_humans package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("dasp_ai_agents_cowriting_humans", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="dasp_ai_agents_cowriting_humans",
    url="https://github.com/oe2015/DASP_AI_Agents_CoWriting_Humans/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="author_name",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["dasp_ai_agents_cowriting_humans = dasp_ai_agents_cowriting_humans.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-dev.txt")},
)
