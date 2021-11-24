// displays image name when image changed
$('#id_image1').change(function() {
    let file = $('#id_image1')[0].files[0];
    $('#filename').text(`Image will be set to: ${file.name}`);
});

// displays image name when second image changed
$('#id_image2').change(function() {
    let file = $('#id_image2')[0].files[0];
    $('#filename2').text(`Image will be set to: ${file.name}`);
});

// displays image name when third image changed
$('#id_image3').change(function() {
    let file = $('#id_image3')[0].files[0];
    $('#filename3').text(`Image will be set to: ${file.name}`);
});