
function toggle2(showHideDiv, switchTextDiv) {
	 var ele = document.getElementById(showHideDiv);
	 var text = document.getElementById(switchTextDiv);
	 if(ele.style.display == "block") {
    		ele.style.display = "none";
		text.innerHTML = "show";
  	}
	 else {
		ele.style.display = "block";
		text.innerHTML = "hide";
	}
}
function toggle3(contentDiv, controlDiv) {
        if (contentDiv.constructor == Array) {
                for(i=0; i < contentDiv.length; i++) {
                     toggle2(contentDiv[i], controlDiv[i]);
                }
        }
        else {
               toggle2(contentDiv, controlDiv);
        }
}