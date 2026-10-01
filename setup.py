from setuptools import setup, find_packages


setup(
    name="project-b-utils",
    version="1.0.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    author="Вячеслав Ребриков",
    description="Утилиты для работы с датами, строками и файлами",
    python_requires=">=3.8",
)