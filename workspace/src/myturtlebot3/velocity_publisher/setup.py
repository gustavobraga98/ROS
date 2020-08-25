from setuptools import setup

package_name = 'velocity_publisher'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gustavo',
    maintainer_email='gustavo@todo.todo',
    description='Pacote criado com intenção de aprender a programar meus próprios pacotes do turtlebot3',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'velocity_publisher = velocity_publisher.velocity_publisher:main' 
        ],
    },
)
