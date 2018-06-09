
var croppieFieldName = "photo";  //change this to system variable
// var croppieOptions = "{{ widget.croppie_options|safe }}";
var element = document.getElementById('cropper');
var orientate_image = 0;
$('#id_' + croppieFieldName + "_5").val(orientate_image);
var cropper = new Croppie(element, {
    viewport: { width: 162, height: 100 },
    boundary: { width: 300, height: 300 },
    showZoomer: true,
    enableOrientation: true
}
);

var cropperCreatedEvent = new Event('cropper-created');

function readFile(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            cropper.bind({
                url: e.target.result,
            });
            document.dispatchEvent(cropperCreatedEvent);
        }
        reader.readAsDataURL(input.files[0]);
    }
}

var photoInput = document.getElementById('id_' + croppieFieldName + '_0');
photoInput.addEventListener('change', function() {
    readFile(this);
    $('#rotate_image').prop('disabled', false);
    track_orientation(0);
});

element.addEventListener('update', function(cr) {
    var data = cropper.get();
    var baseSelector = 'id_' + croppieFieldName + '_';
    var pointInput = null;
    for (var i = 1; i <= 4; i++) {
      console.log("coordinates")
      pointInput = document.getElementById(baseSelector + i)
      pointInput.value = data.points[i-1];
      console.log(data.points[i-1] )
    }
});

$('#rotate_image').on('click', function(ev) {
    cropper.rotate(parseInt($(this).data('deg')));
    var baseSelector = 'id_' + croppieFieldName + '_5';
    track_orientation(1);
    $('#'+ baseSelector).val(orientate_image)
    console.log(orientate_image)
});

function track_orientation(x){
    if(x==1){
      orientate_image = orientate_image + 1
    } else {
      orientate_image = 0
    }
    if (orientate_image >= 4){
      orientate_image = orientate_image-4
    }
};
