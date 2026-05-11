# this will copy the base image or I will say that it will make use of pyhton base image 3.10-slim.
FROM python:3.10-slim 
# sets the current working directory to /app
WORKDIR /app
# copy all the dependencies from requirement.txt to current working directory i.e /app (.)
COPY requirements.txt . 
# during build install all the pyhton dependencies listed in requirements.txt without saving any temporary download cache.
RUN pip install --no-cache-dir -r requirements.txt
#copy all the local files into /app
COPY . . 
# expose port 3000
EXPOSE 3000
#in simple words it means when container starts run the python file main.py
CMD [ "python" , "main.py" ]


