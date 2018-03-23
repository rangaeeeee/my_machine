sudo apt-get update

## python related installations
sudo apt-get install python3
sudo apt-get install python-pip
sudo apt-get install python3-pip
sudo apt-get install spyder

## emacs editor
sudo apt-get install emacs

## git for source code control
sudo apt-get install git

## video screen recorder
sudo add-apt-repository ppa:maarten-baert/simplescreenrecorder
sudo apt-get update
sudo apt-get install simplescreenrecorder simplescreenrecorder-lib

## krita - drawing tool
sudo add-apt-repository ppa:kritalime/ppa
sudo apt-get update
sudo apt-get install krita

## Latex 
sudo apt-get install texlive

## java installation
sudo apt-get install jre

## GIMP
sudo apt-get purge gimp
sudo apt-get install ppa-purge
sudo apt-get ppa:otta-kesselgulasch/gimp
sudo apt-get ppa:otta-kesselgulasch/gimp-edge
sudo apt-get update
sudo apt-get install gimp

## Inkscape
sudo add-apt-repository ppa:inkscape.dev/stable
sudo apt-get update
sudo apt-get install inkscape

## latex packages
sudo apt-get install texlive-full
sudo apt-get install xzdec
sudo tlmgr init-usertree
sudo apt-get install tk
sudo tlmgr install amsmath
sudo tlmgr install pgf 

# Python packages
sudo apt-get install python-pip
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
sudo pip install -U nltk
