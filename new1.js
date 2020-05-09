  
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
				$("#myimage").attr("src", data.iurl);
			}	

		});

		event.preventDefault();

	});

});
