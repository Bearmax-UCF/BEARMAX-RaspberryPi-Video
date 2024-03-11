FROM python:3.11

# Set up container

RUN addgroup -S video \
    && adduser -S -G video video \
    && mkdir -p /home/app \
    && chown -R video:video /home/app

USER video:video

WORKDIR /home/app

COPY --chown=video:video . .

# Install dependencies

RUN pip install -r requirements.txt

# Run the application

ENTRYPOINT ["python3"]
CMD ["videoDisplay.py"]
