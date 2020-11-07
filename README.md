# NLTK_Tools

Got my hands on a lot of plain text books for training ML from bookcorpus and didn't know what all to do with them.

I hadn't experimented much with grep and quickly wore that out on the files. Then, I eventually moved on to NLTK for something more to do.

Feel free to add more plain text books to the `\epubtxt\` directory and change the path variable within `main.py` to the desired book. 

## Uses

* Tokenize plain text books into words, cleans the words, then you can create frequency distribution plots and/or word clouds. 

## Requirements

* [WSL](https://docs.microsoft.com/en-us/windows/wsl/about)
* [Docker](https://docs.docker.com/docker-for-windows/install/)
* [VcXsrv](https://sourceforge.net/projects/vcxsrv/)
* [Setup your Windows Firewall For VcXsrv](https://github.com/microsoft/WSL/issues/4106#issuecomment-667746865)

## Preliminary Setup
1. Launch XLaunch (you got this when you installed VcXsrv), choose multiple windows, start no client, select Disable access control, add the additional parameters "-ac" (no quotes)
2. run `git clone https://github.com/LewkyB/NLTK_Tools.git`
3. `cd NLTK_Tools`
4. run `docker build -t lewkb/nltktool:1.0 .`
5. run `docker run -ti --rm -e DISPLAY=$DISPLAY --name nl lewkb/nltktool:1.0`

If after running you received the error similiar to "_tkinter.TclError: couldn't connect to display "192.168.1.1:0.0"" you will you need changed your `$DISPLAY` variable in your `~/.bashrc`. 

I solved this by running `ipconfig /all` in `cmd.exe` and trying all the listed IPv4 addresses. I initially tried using `export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0` in my `~/.bashrc`, but for some reason with my WSL1 the only nameserver I pull is `8.8.8.8`. You can quickly test differnt IPv4 addresses by just entering `export DISPLAY="your IPv4 address here":0.0` (ex. `export DISPLAY=192.168.0.0.1:0.0`). Run `docker run -ti --rm -e DISPLAY=$DISPLAY --name nl lewkb/nltktool:1.0` each time you change the `$DISPLAY`.

## Download the plain txt books

Downloads are all very fast. 

* [download for 2gb zip that unpacks to 6gb, about 19000 books](https://the-eye.eu/public/AI/pile_preliminary_components/books1.tar.gz)
* [download the 37gb monster with 197000 books](https://the-eye.eu/public/AI/pile_preliminary_components/books3.tar.gz)
* [links are courtesy of this comment on Github](https://github.com/soskek/bookcorpus/issues/27#issuecomment-716104208)

## Python Packages

* [NLTK](https://www.nltk.org/)
* [word_cloud](https://github.com/amueller/word_cloud)


## Other resources

https://github.com/NirantK/nlp-python-deep-learning

https://github.com/keon/awesome-nlp#user-content-python
