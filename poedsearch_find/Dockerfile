from ubuntu:18.04

RUN apt-get -yqq update
RUN apt-get -yqq install coreutils
RUN apt-get -yqq install python3
RUN apt-get -yqq install python3-pip
RUN apt-get -yqq install netcat
RUN pip3 install argparse
RUN pip3 install mysql-connector-python
RUN pip3 install requests


ADD find_new.py /opt/

WORKDIR /opt/
CMD sleep 15 && ./find_new.py  
#CMD service mysql start && while true; do echo "1";done


