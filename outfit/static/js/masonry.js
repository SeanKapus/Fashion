$(document).ready(function() {
//upload image button
    $('#clothes').on('click', function() {
        $('#topform').toggle();
    });
//// get images for divs
//    $.ajax({
//        url: "/getall/",
//        type: "GET",
//        dataType: "json",
//
//        success: function(data) {
//            console.log(data);
//            console.log(window.location);
////            for (var i = 0; i < data.length; i++) {
////                $('#container_tops').html('<img src=' + window.location.origin + '/static/media/' + data[i].fields.image + '/>');
//            },
//            error: function(data) {
//                console.log(data);
//            }
//
//    });
//    $( "#container_tops" ).draggable({
//        start: function() {
//            $('#dragDocs').show();
//        },
//        stop: function() {
//            $('#dragCode').show();
//        }
//    });
//    $("#columnTwo").droppable({
//        accept: "#drag",
//        over: function () {
//            $('#dropDocs').show();
//        },
//        drop: function () {
//            $('#dropCode').show();
//        }
//    });
//close js
});