$(document).ready(function() {

	$('#searchForm').on('submit', function(event) {
		
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

	$('#addSeriesForm').on('submit', function(event) {
		
		$.ajax({
			data : {
				name : $('#sName').val(),
				description : $('#Sdescription').val(),
				hero : $('#sHero').val(),
				image: $('#sImage').val(),
				url: $('#sUrl').val(),
				date: $('#sDate').val(),
				menuid: $('#sMenuId').val()
				
			},
			type : 'POST',
			url : '/addprocess'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlertAdd').text(data.error).show();
				$('#successAlertAdd').hide();
				$('#udContiner2').hide();
				
			}
			else {
				$('#successAlertAdd').show();		
				$('#sucessTextAddSeries').text(respond.name).show();
				$('#errorAlertAdd').hide();				
                let addurl = "url('" + data.iurl + "')" 		
                $("#successAlertAdd").css("background", addurl);
			}	

		});

		event.preventDefault();

	});
	
	$('#movieform').on('submit', function(event) {
		
		$.ajax({
			data : {
				mname : $('#mName').val(),
				mdescription : $('#mDescription').val(),
				mhero : $('#mHero').val(),
				mimage: $('#mImage').val(),
				murl: $('#mUrl').val(),
				mdate: $('#mDate').val(),
				mmenuid: $('#mMenuId').val()
				
			},
			type : 'POST',
			url : '/movieprocess'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlertAdd').text(data.error).show();
				$('#successAlertMovie').hide();
				$('#udContiner2').hide();
				
				
			}
			else {
				$('#successAlertMovie').show();		
				$('#sucessTextAddMovie').text(respond.name).show();
				$('#errorAlertAddMovie').hide();				
                let addurl = "url('" + data.iurl + "')" 		
                $("#successAlertMovie").css("background", addurl);
				
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



