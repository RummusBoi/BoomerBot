FROM python:3
RUN pip install matplotlib
RUN pip install numpy
RUN pip install bs4
RUN pip install tensorflow
RUN /bin/bash -c "git clone https://github.com/philbot9/youtube-comment-scraper.git /proj/youtubescraper"