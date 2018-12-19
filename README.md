# TOC Project 2019

Template Code for TOC Project 2019

A Facebook messenger bot based on a finite state machine

More details in the [Slides](https://hackmd.io/p/SkpBR-Yam#/) and [FAQ](https://hackmd.io/s/B1Xw7E8kN)

## Setup

### Prerequisite
* Python 3
* Facebook Page and App
* HTTPS Server

#### Install Dependency
```sh
pip3 install -r requirements.txt
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)

#### Secret Data

`VERIFY_TOKEN` and `ACCESS_TOKEN` **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

#### Run Locally
You can either setup https server or using `ngrok` as a proxy.

**`ngrok` would be used in the following instruction**

```sh
./ngrok http 5000
```

After that, `ngrok` would generate a https URL.

#### Run the sever

```sh
python3 app.py
```

## Finite State Machine
![fsm](./img/show-fsm.png)

## Usage
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.

* user
	* Input: "go to state1"
		* Reply: "I'm entering state1"

	* Input: "go to state2"
		* Reply: "I'm entering state2"


## Reference
[TOC-Project-2017](https://github.com/Lee-W/TOC-Project-2017) ❤️ [@Lee-W](https://github.com/Lee-W)
# Facebook_Chatbot


由圖可知總共有10個state
initial:user
輸入
“你好”
進入hellow
你有三個選擇可以以選，分別為
1.申購資訊（state1)
2.匯率查詢（state4)
3.k線教學（state6)

申購資訊
	將列出目前所有“可申購”以及“申購中“的股票
	再輸入此股票的
	”(股號)“
	即可獲得詳細資訊（state2)
	如果想知道更多詳細資訊輸入
	”想知道更多“
	會將個股網址回傳（state3)
	再回到user state
匯率查詢
	將印出前8筆常用買賣匯率
	輸入欲查詢的
	“(幣種)”
	列出當日買進賣出資訊（state5)
	再回到user state
k線教學
	各自輸入
	“陽線”（state7)
	或
	“陰線”（state8)
	可得相關圖解
	再回到user state