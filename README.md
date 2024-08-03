## Bachelor degree final project demo
----------------------
This is a demo of a Patent Search Engine web-app based on T5 and BERT-like large language models (LLMs) that allow to enter a query in Russian/English/Chineese and retrieve relevant data in the domain of English language patents (test data scraped from Google Patents).

Installation of this demo is fully automated with Docker. 

[Advanced] Deployment of this web-app to remote server is also fully automated with the help of Ansible-playbook scripts and Docker Compose for Nginx and Cerbot.

[Currently expired!] Public access is granted by following www.patent-search.online

----------------------

Installation & Running locally without Docker (not recommended)
-------------
1. Clone the repo and create a venv
1. Install the required Python packages by running `pip install --ignore-installed -r requirements.txt` OR simply run the `run.sh` script [windows]: `bash .\run.sh` OR [unix/linux]: `.\run.sh`.
2. Configure model_config.yaml [optional]
3. Download Hugging Face models by running `python3 model_utils.py`
4. Run the Python Flask application by running `python3 app.py`.
5. Open a web browser and click to some kind of `http://***.*.*.*:2000` link in terminal to access the Patents&Suppliers Search Service.
6. Enter a query in the search box and click "Search" to retrieve relevant patent documents and potential suppliers.


Installation & Running locally with Docker (recommended)
-----
1. Clone the repo and `cd Patent-Search`
2. Configure model_config.yaml [optional]
3. Run `docker build -t patent-search .` to create an image.
4. After building an image simply run `docker run patent-search`
5. In the terminal follow one of the links to access Patents&Suppliers Search Service.
6. Enter a query in the search box and click "Search" to retrieve relevant patent documents and potential suppliers.

Author
------
Vladislav Gromadskii

 
