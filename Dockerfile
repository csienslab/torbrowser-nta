FROM ubuntu:18.04

MAINTAINER jimmy r08922004@ntu.edu.tw
COPY . /root/
RUN mv /root/code /root/nslab && mv /root/Data /root/nslab/Data
WORKDIR /root/nslab
RUN ["./setup.sh","10","docker"]
ENTRYPOINT ["/root/nslab/openworld.sh"]
CMD ["1000,2000"]