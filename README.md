股市申購以及匯率查詢
==================
FSM圖

![Markdown](https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.0-9/48358301_2227569273931472_7019101456548495360_o.jpg?_nc_cat=100&_nc_ht=scontent.fkhh1-1.fna&oh=43710b12558648e55df1d74fd2763491&oe=5CD984BE)

**NOTE:** 總共有10個state
initial state:user


操作流程
================
輸入
“你好”
進入<hellow>state
你有三個選擇可以以選，分別為
*   1.申購資訊<state1>
*   2.匯率查詢<state4>
*   3.k線教學<state6>
	
並鍵入所需要服務字串

example:
	
	"申購資訊"
	
	
	
<h2 id="overview">申購資訊</h2>
將列出目前所有“可申購”以及“申購中“的股票

再輸入此股票的:
		
	”(股號)“
example:
	
	"3321"
	
即可獲得詳細資訊<state2>
	
如果想知道更多詳細資訊輸入:

	”想知道更多“

會將個股網址回傳<state3>
	
再回到user state

<h2 id="overview">匯率查詢</h2>
印出前8筆常用買賣匯率

輸入欲查詢的:
	
	“(幣種)”
	
example:
	
	"美金"
列出當日買進賣出價格<state5>
	
再回到user state
	
<h2 id="overview">k線教學</h2>
各自輸入

	“陽線”<state7>
或

	“陰線”<state8>
可得相關圖解

再回到user state
