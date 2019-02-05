from ubuntu:18.04

RUN apt-get -yqq update
RUN apt-get -yqq install coreutils
RUN apt-get -yqq install mysql-server
RUN apt-get -yqq install python3
RUN apt-get -yqq install python3-pip
RUN pip3 install requests
RUN pip3 install mysql-connector-python
RUN apt-get -yqq install vim
RUN apt-get -yqq install net-tools
RUN apt-get -yqq install netcat
ADD poeid.sql /opt/

COPY mysqld.cnf /etc/mysql/mysql.conf.d/mysqld.cnf
RUN /etc/init.d/mysql start && /etc/init.d/mysql status && echo "1" && mysql -u root -e 'SHOW DATABASES;' && mysql -u root -e 'create database POEID;' && mysql -u root -e "create user poe@'%' identified by 'wantmore';" && mysql -u root -e "grant all on POEID.* to poe@'%';" && mysql -u root -e "flush privileges;" && mysql -u root POEID < /opt/poeid.sql

ADD get_id_new.py /opt/
ADD find_new.py /opt/
#COPY mysqld.cnf /etc/mysql/mysql.conf.d/mysqld.cnf

WORKDIR /opt/
#EXPOSE 3306:3306
CMD service mysql start && ./get_id_new.py  
#CMD service mysql start && while true; do echo "1";done


