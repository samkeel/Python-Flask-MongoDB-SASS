from setuptools import find_packages
from setuptools import setup


setup(
    name="crud_n_sass",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["flask"],
    setup_requires=['libsass >= 0.6.0'],
    sass_manifests={
        'crud_n_sass': ('static/sass', 'static/css', '/static/css')
    }
)
