#!usr/bin/env python
# -*- coding:utf-8 -*-

from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSER = 'smtp.163.com'
POPSER = 'pop3.163.com'

origHdrs = ['From:','','']

