git fetch origin

git checkout -b experimental origin/experimental

git merge Master
RUN chmod 777 /root/userbot
WORKDIR /root/userbot/

EXPOSE 80 443

CMD ["python3","-m","userbot"]
