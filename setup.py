from setuptools import find_packages, setup

# python3 setup.py bdist_wheel
# pip install dist/ai_lib-0.1.0-py3-none-any.whl
# when renaming, delete all the files change import calls, reinstall

setup(
    name='ai_lib',
    packages=[
        'ai_lib', 'ai_lib.nn', 'ai_lib.core_math'
    ],
    version='0.1.0',
    description='ai_lib',
    author='asds',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)