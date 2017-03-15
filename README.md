# timetoy
A very minimal chronometer for android.

To run it on PC: 

```shell

# create virtual env
virtualenv /tmp/timetoyenv
source /tmp/timetoyenv/bin/activate
# clone
git clone https://github.com/gstsistemas/timetoy
cd timetoy
# install requirements
pip install -r requirements.txt
python main.py

```

You can build an APK with buildozer as follows:


```shell

cd timetoy
buildozer android debug

```

I suggest using https://github.com/gstsistemas/buildozo/ to build the APK.
