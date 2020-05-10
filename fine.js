  

$(document).ready(function() {

	$('form').on('submit', function(event) {
		
		$.ajax({
			data : {
				search : $('#nameInput').val(),
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
				
			}
			else {
				$('#successAlert').show();		
				$('#sucessText').text(data.name).show();
				$('#errorAlert').hide();
				$("#mylink").attr("href", data.search);
                let myurl = "url('" + data.iurl + "')" 		
                $("#successAlert").css("background", myurl);
			}	

		});

		event.preventDefault();

	});

});


var hider = document.getElementById("#udContiner");

$(document).ready(function(){
  $("#searchbtn").click(function(){
  
  let test = $('#txt_search').val();
  if (test != '') {
    $("#udContiner").toggle();
    }
  if (test == '') {
    $("#udContiner").hide();
    }  
  });
});

var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
