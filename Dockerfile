FROM anibali/pytorch


# Set the working directory within the container
RUN mkdir app
WORKDIR /app

RUN mkdir templates && mkdir indexed
COPY templates templates
COPY indexed indexed

# Copy necessary files to the container
COPY ./src/app.py ./src/model_utils.py requirements.txt ./src/lang_processor.py ./src/search.py run.sh model_config.yaml ./


RUN pip install -r requirements.txt && python3 model_utils.py

EXPOSE 2000

ENTRYPOINT ["python3"]

CMD ["app.py"]
