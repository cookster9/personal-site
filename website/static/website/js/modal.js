// Get the modals
var modals = document.querySelectorAll(".modal");

// Get all divs that open a modal
var jobDivs = document.querySelectorAll('.welcome-job-button');
jobDivs.forEach((div) => {
	div.addEventListener('click', (e) => {
		showModal(e.target.id);
		});
	});

// When the user clicks on the div, open the modal
function showModal(id) {
    modals.forEach((modal) =>{
        if(modal.classList.contains(id)) modal.style.display = "block";
    })
}

// When the user clicks on <span> (x), close the modal
var jobSpans = document.querySelectorAll('.close');
jobSpans.forEach((span) => {
    span.addEventListener('click', (e) => {
		closeModalWithSpan(span);
		});
})

function closeModalWithSpan(span){
    span.parentNode.parentNode.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    modals.forEach((modal) => {
        if (event.target == modal) {
            modal.style.display = "none";
          }
    })
}