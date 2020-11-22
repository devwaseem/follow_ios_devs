![](https://github.com/devwaseem/follow_ios_devs/raw/main/screenshots/banner.png)
# follow_ios_devs
A Python script to follow iOS developers/community on twitter automatically

![Python](https://img.shields.io/badge/Language-Python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/devwaseem/follow_ios_devs/blob/main/LICENSE)
![GitHub forks](https://img.shields.io/github/forks/devwaseem/follow_ios_devs?label=Fork&style=social)
![GitHub Stars](https://img.shields.io/github/stars/devwaseem/follow_ios_devs?label=Stars&style=social)
![GitHub Watchers](https://img.shields.io/github/watchers/devwaseem/follow_ios_devs?label=Watchers&style=social)


[![Twitter URL](https://img.shields.io/twitter/url?style=social&url=https://github.com/devwaseem/follow_ios_devs)](http://twitter.com/share?text=Follow+other+ios+devs+out+there+using+this+script+created+by+@iamwaseem99&url=https://github.com/devwaseem/follow_ios_devs&hashtags=swiftui,ios,iphone,news,github,iosdevelopers,swift,xcode)
[![Twitter Follow](https://img.shields.io/twitter/follow/iamwaseem99?style=social)](https://twitter.com/iamwaseem99)

![](https://github.com/devwaseem/follow_ios_devs/raw/main/screenshots/screen1.png)
 
## 📜 Requirements
```
- Python3
- Safari
- Selenium
```
## 🔧 Installation
```
git clone https://github.com/devwaseem/follow_ios_devs.git
cd follow_ios_devs/
make setup
```

## ⚙️ Configuration

Make sure you add your twitter username and password in `config.py` file inorder for the script to work.

To add or delete twitter handles, refer `handles.json` file. 

**Can't see your name in the file? feel free to pull request to get your name added to the list.**

| Variable      | default       | description                                           |
| ------------- |:-------------:| :-----------------------------------------------------|
| USE_EMOJI     | True          | if your terminal doesn't support emoji, make it False |
| WAIT_TIME     | 3             | adjust time in seconds based on your internet speed   |
| USERNAME      | empty string  | twitter username                                      |
| PASSWORD      | empty string  | twitter password                                      |


## How to Run

In terminal, inside the project folder, type:

```
./follow_ios_devs.py
```




## ✏️ Contribute

If you want to contribute to this library, you're always welcome!

### What you can do
You can contribute us by filing issues, bugs and PRs.

### Contributing guidelines:
- Open issue regarding proposed change.
- Repo owner will contact you there.
- If your proposed change is approved, Fork this repo and do changes.
- Open PR against latest `dev` branch. Add nice description in PR.
- You're done!

## ⚖️ [License](https://github.com/devwaseem/follow_ios_devs/blob/main/LICENSE)

```
MIT License

Copyright (c) 2020 TheCodeMonks

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
