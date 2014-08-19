/**
 * Created by SeanK on 8/14/14.
 */
$(document).ready(function () {
    $('#clothes').on('click', function() {
        $('#topform').toggle();
    });

    $(".draggable_top").draggable({
        drag: function () {
           console.log("dragging");
        }
    });
    $( ".droppable_top" ).droppable({
        drop: function( event, ui ) {
            console.log("dropped!");
        }
    });

    $(".draggable_bottom").draggable({
        drag: function () {
           console.log("dragging");
        }
    });
    $( ".droppable_bottom" ).droppable({
        drop: function( event, ui ) {
            console.log("dropped!");
        }
    });

    $(".draggable_headwear").draggable({
        drag: function () {
           console.log("dragging");
        }
    });
    $( ".droppable_headwear" ).droppable({
        drop: function( event, ui ) {
            console.log("dropped!");
        }
    });

    $(".draggable_shoes").draggable({
        drag: function () {
           console.log("dragging");
        }
    });
    $( ".droppable_shoes" ).droppable({
        drop: function( event, ui ) {
            console.log("dropped!");
        }
    });

    $(".draggable_accessories").draggable({
        drag: function () {
           console.log("dragging");
        }
    });
    $( ".droppable_accessories" ).droppable({
        drop: function( event, ui ) {
            console.log("dropped!");
        }
    });
});