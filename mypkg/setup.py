from setuptools import setup

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tsubo',
    maintainer_email='git.otsubokura@gmail.com',
    description='stop system',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = mypkg.talker:mian',
            'listener = mypkg.listener:main'
        ],
    },
)
