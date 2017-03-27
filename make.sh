cd @@PATH_TO_THIS_FILE;
wget -O @@NAME_OF_FILE.csv https://@@GOOGLE_DOC_LINK_TO_FILE/export?format=csv;
python make.py;
sudo service nginx restart;
