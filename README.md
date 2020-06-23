# Chatbot--Stack-Overflow-Assistant
Natural Language Processing is used to construct a dialogue chat bot, which will be able to  answer programming-related questions (using StackOverflow dataset), and  chit-chat and simulate dialogue on all non programming-related questions.

AWS Hosted Telegram bot:

How to create/update the bot code:

1. The python codes used are :
a. Python notebbok that trains models.
b. utils.py
c. dialogue_manager.py
d. main_bot.py = driver or main file.

2. SSH into AWS instance -> start tmux session -> Use docker-> run main_bot.py using telegram token.

i. To be able to access IPython notebooks running on AWS, you might want to SSH with port tunneling:

ssh -L 8080:localhost:8080 -i path/to/private_key(local .pem or .ppk file) ubuntu(AWS username)@ec2-XX-XXX-X-XX.us-east-2.compute.amazonaws.com(public DNS)

Exact command: ssh -L 8080:localhost:8080 -i SurabhiNLPProject.pem ubuntu@ec2-18-191-89-38.us-east-2.compute.amazonaws.com

Then you will be able to see the notebooks on localhost:8080 from your browser on the local machine.

ii. Send code and data to AWS instance:

I used WinSCP for this. To setup WINSCP session: use SFTP protocol, Host name in Amazon Public DNS, Port is 22 and USername is ubuntu. Password leave blank. Go to advanced and SSH -> Authentication -> choose pem [or better ppk] file.

In the newly created session, transfer/copy files using drag and drop.

iii. sudo apt-get install tmux 
tmux new -s my_awesome_session
####you live here
tmux detach

tmux attach -t my_awesome_session
#####you come back here tomorrow

Exact command (tmux installed earlier) : tmux new -s my_awesome_session

This will ensure that your session (and the running bot) will be kept alive even even if you loose your connection. Thus the usual order would be: ssh -> tmux -> docker -> python.

iv. Set up docker on AWS instance. This is a one-time setup for an AWS instance. I used an available docker image with required python dependencies to run the main_bot.py code in the container.

v. Mount data and code from AWS instance to docker and start the container (use run for new container, rm to delete container and exec for existing container)

docker run -it -p 8080:8080 --name coursera-aml-nlp -v $PWD:/root/coursera akashin/coursera-aml-nlp

Exact commands used: 

docker stop coursera-aml-nlp (if already running container)
docker rm coursera-aml-nlp (to recreate same container in next step after removing it in this step)
docker run -it -p 8080:8080 --name coursera-aml-nlp -v $PWD:/root/coursera akashin/coursera-aml-nlp

Any changes done on copies of file at AWS instance will be sent automatically on docker file also as it is shared files not copied files. So to modify code, modifying on AWS instance is enough (in WinSCP or localhost:8080 connecting to AWS instance)

Got the console window in docker - can run python code, open jupyter notebook etc.

v. Take token from telegram bot and python3 main_bot.py --token=YOUR_TOKEN on docker terminal.

GO to appropariate directory where main_bot.py is stored and then run:
cd coursera
cd CodeGuru
pip install scikit-learn==0.22.2.post1 [-- unpickling sklearn files as pickling used this version].
python3 main_bot.py --token=<token>

Note: data and thread_embeddings_by_folder have been moved to hard disk "NLP_Course_Coursera" -> Chatbot folder. GitHub has size restrictions and hence do not allow those files.
