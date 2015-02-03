

function checkBgState(){
	bg = document.getElementById('ch_bg')
	off =document.getElementById("off")
	on = document.getElementById("on")
	console.log(sessionStorage.getItem("bgState"));
	if (sessionStorage.getItem("bgState") == "false") {
		bgOff();
	}
	else{
		bgOn();
	}

}
function bgOn(){

	bg.src="static/pic/bg.jpg";
	bg.style.display="block";
	off.style.color="white";
	on.style.color="#51AABC";
	sessionStorage.setItem("bgState", "true");
	console.log(sessionStorage.getItem("bgState"));
	}
function bgOff(){
	bg.style.display="none";
	off.style.color="red";
	on.style.color="white";
	sessionStorage.setItem("bgState", "false");
	console.log(sessionStorage.getItem("bgState"));
	}
