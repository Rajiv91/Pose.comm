import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='posecomm',
    version='0.0.1',
    author='Rajiv Gonzalez',
    author_email='rajiv@tryiris.ai',
    description='Package for the ipc communication between the pose estimator and the autotracking',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Rajiv91/Pose.comm.git',
    project_urls = {
        "Bug Tracker": "https://github.com/Rajiv91/Pose.comm/issues"
    },
    license='MIT',
    packages=['posecomm'],
    install_requires=['aio-udp-server'],
)