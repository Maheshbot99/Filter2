if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Maheshbot99/Filter2 /Filter2
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Filter2
fi
cd /Filter2
pip3 install -U -r requirements.txt
echo "Starting Filter2...."
python3 bot.py
