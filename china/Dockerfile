FROM ubuntu:18.04
RUN apt-get update && apt-get install sudo software-properties-common -y
RUN sudo add-apt-repository ppa:gophers/archive && sudo apt-get update && apt-get -y upgrade
RUN sudo apt-get install git emacs-nox python3-pip ipython3 -y
RUN cd /home && git clone -b release/v3.2.7 https://github.com/alpacahq/marketstore.git && git clone https://github.com/alpacahq/pymarketstore.git && git clone https://github.com/quantopian/trading_calendars.git && git clone https://github.com/quantopian/zipline.git
# RUN cd /home/marketstore && make vendor &&  make install &&  make plugins
RUN cd /home/trading_calendars && pip3 install .
RUN cd /home/zipline && pip3 install -e .
RUN cd /home && mkdir china
COPY * /home/china/
RUN cd ~ && mkdir .zipline && cp /home/china/china_calendar_setup.py ~/.zipline/extension.py
RUN cd /home/china/ && mkdir data && mv daily/ data/
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8



