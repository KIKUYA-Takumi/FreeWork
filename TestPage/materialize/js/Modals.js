$(document).ready(function(){
    // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
    $('.modal-trigger').leanModal();
  });
$('#modal1').openModal();
$('#modal1').closeModal();

$('#modal2').openModal();
$('#modal2').closeModal();