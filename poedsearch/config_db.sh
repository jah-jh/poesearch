#!/bin/sh

mysql -u root -e "create database POEID;"
mysql -u root -e "create user 'poe'@'%' identified by 'wantmore';"
mysql -u root -e "grant * on POEID.* to 'poe'@'%';"
mysql -u root -e "flush privileges;"
