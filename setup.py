from setuptools import setup, find_packages

setup(
    name='aigency_api',
    version='0.1.0',
    packages=find_packages(),  # Burada find_packages() tüm alt paketleri bulur
    install_requires=[
        'requests',
        'colorama'
    ],
    entry_points={
        'console_scripts': [
            'aigency_api=aigency_api.cli:main'
        ]
    },
    author='eCloud Tech.',
    author_email='info@e-cloud.web.tr',
    description='API client library for interacting with Aigency API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ecloud-bh/aigency_api',
    python_requires='>=3.6'
)
