# We use the basic Python 3 image as our launching point.
FROM python:3
# We want to run a basic Python script which we’ll call my_script.py. First, we need to add the script to the Dockerfile:
ADD my_script.py /
# We want to run a basic Python script which we’ll call my_script.py. First, we need to add the script to the Dockerfile:
# Our script depends on pandas, so install this
RUN pip install pandas
# Add this line to your Dockerfile to execute the script:
CMD [ "python", "./my_script.py" ]