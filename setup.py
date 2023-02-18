import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='PoseEstimatorComm',
    version='0.0.1',
    author='Rajiv Gonzalez',
    author_email='rajiv@tryiris.ai',
    description='Package for the ipc communication between the pose estimator and the autotracking',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/tryiris-ai/Pose.estimator.comm.git',
    project_urls = {
        "Bug Tracker": "https://github.com/tryiris-ai/Pose.estimator.comm/issues"
    },
    license='MIT',
    packages=['PoseEstimatorComm'],
    install_requires=['aio-udp-server'],
)