FROM python:3
WORKDIR /usr/src/app
#Copy the file from this machine to the new machine.
COPY requirments.txt .

#Install the packages to the new machine
RUN pip3 install --no-cache-dir -r requirments.txt
# Copy current files "requirments.txt and app.py" into the system at WORKDIR
# First . is what is in your machine,
# Second . What's going into the machine.
# Copy all the files from local machine to the new machine
COPY . .
#Command to tell the docker to run the file.
CMD ["python", "app.py"]