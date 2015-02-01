

function checkBgState(){
	bg = document.getElementById('ch_bg')		//Osäker om det är OK att deklarera globala variablar här??
	off =document.getElementById("off")
	on = document.getElementById("on")
	cur = document.getElementById("curiosities")
	center = document.getElementsByClassName('center')
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
	if (screen.width < 1250) {
    	cur.style.display="none";
	} else {
    	cur.style.display="block";
	}
	sessionStorage.setItem("bgState", "true");
	console.log(sessionStorage.getItem("bgState"));
	}
function bgOff(){
	bg.style.display="none";
	off.style.color="red";
	on.style.color="white";
	sessionStorage.setItem("bgState", "false");
	cur.style.display="none";
	console.log(sessionStorage.getItem("bgState"));
	}
function showOnlyBg(){

	cur.style.display="none";
	center[0].style.display="none"; //retunerar en array därav [0] index
}