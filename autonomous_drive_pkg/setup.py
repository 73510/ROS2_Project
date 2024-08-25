from setuptools import setup

package_name = 'autonomous_drive_pkg'

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
    maintainer='uugh73510',
    maintainer_email='uugh73510@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'autodrive = autonomous_drive_pkg.autodrive:main', 
            'autodrive_client = autonomous_drive_pkg.autodrive_client:main'
        ],
    },
)

            