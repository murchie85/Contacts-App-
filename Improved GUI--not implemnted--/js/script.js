$(document).ready(function(){
	// show loader image 
	$('#loaderImage').show()


	// show contacts on page load
	showContacts();

});

//show contacts 
function showContacts(){
	console.log('showing contacts....')
	setTimeout("$('#pageContent').load('contacts.php', function(){$('loaderImage').hide()})", 1000);
}