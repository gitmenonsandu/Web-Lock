var Ele1,Ele2,Ele3,Ele4,Ele5;
document.addEventListener('DOMContentLoaded', function () {
	console.clear();
	console.log("popup.js loaded");
	var disableFlag;
	chrome.storage.local.set({'disableFlag' : 0});

	Ele1 = document.querySelector('.op1');
	Ele1.addEventListener("click", op1mscl);
	
	Ele2 = document.querySelector('.op2');
	Ele2.addEventListener("click", op2mscl);
	
	Ele3 = document.querySelector('.op3');
	Ele3.addEventListener("click", op3mscl);
	
	Ele4 = document.querySelector('.op4');
	Ele4.addEventListener("click", op4mscl);
	
	
});

function op1mscl(){
	console.log("Calling background lock function");
	var disableFlag;
	var yellowCode="248057";

	//runs asynchronous. have to change.
		chrome.storage.local.get('disableFlag',function(d){
			if(d.disableFlag==1){
				yellowCode="000000";
			}
			else
				yellowCode="248057";
		
		});
	chrome.runtime.sendMessage({method : "codeYellow", code : yellowCode},
		function(response){
			if(response.result == 0){
				console.log("Lock function returned in +ve");
			}else{
				console.log("Lock function returned in -ve");
			}
		}
	);
	window.close();
}

function op2mscl(){

	chrome.tabs.create({
		url: "options.html",
		active: true,
		pinned: false
	});
	window.close();
}

function op3mscl(){
	var newURL = "chrome://extensions/?id=" + chrome.runtime.id;
	chrome.tabs.create({ url : newURL});
	window.close();
}
