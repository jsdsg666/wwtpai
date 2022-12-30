from setuptools import setup, find_packages


setup(
    name='wwtpai',
    version='0.1.1',
    license='GNU GPLv3',
    author="Yuqi Wang",
    author_email='22S054041@stu.hit.edu.cn',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/jsdsg666/wwtpai',
    keywords='wwtpai',
    install_requires=[
        'pandas',
        'openpyxl'
      ],

)
