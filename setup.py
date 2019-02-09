
from setuptools import setup, Distribution, find_packages

setup(name='hackforces',
      version='0.0.1',
      description='Python library for Hackforces project',
      url='http://github.com/hackforces/hackforces-python',
      author='Alexey Rodionov',
      author_email='no-reply@hackforces.com',
      license='GNU Affero General Public License v3 or later (AGPLv3+) (AGPL-3.0)',
      packages=find_packages(exclude=['dist','build','*.pyc', '.DS_Store', '.vscode', '__pycache__', '*.bak']),
      package_data={
            'iroha': ['_iroha.exp', '_iroha.lib', '_iroha.pyd', '_iroha.pyd.manifest', 'bindings.lib', 'libprotobuf.dll', '_iroha.so', '*.py']
      },
      install_requires=[
            'requests>=2.8.0'
      ],
      classifiers=[
            'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python',
            'Operating System :: OS Independent',
            'Environment :: Console',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.5'
      ],
      project_urls={
        "GitHub": "https://github.com/hackforces",
      },
      zip_safe=False,
)

