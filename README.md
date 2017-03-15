# timetoy
A very minimal chronometer for android.

To run it on PC: 

```shell

virtualenv /tmp/timetoyenv
source /tmp/timetoyenv/bin/activate

git clone https://github.com/gstsistemas/timetoy
cd timetoy
python main.py

```

You can build an APK with buildozer as follows:


```shell

cd timetoy
buildozer android debug

```

I suggest using https://github.com/gstsistemas/buildozo/ to build the APK.
