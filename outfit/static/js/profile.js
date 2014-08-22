/**
 * Created by SeanK on 8/14/14.
 */
$(document).ready(function () {
    // Should reuse this code between your two different templates instead of duplicating it
    // You'll want to cleanup all of these console.log statements

//    button to upload clothes to user profile
    $('#clothes').on('click', function() {
        $('#topform').toggle();
    });

//    button to save favorites to users profiles
    $("#btn-start").on("click", function() {
        $.ajax({
          url: $(this).attr("href"),
          data: {pk: $(this).data("pk")},
          success:function(data) {
             console.log("success")
          },
            error: function(data) {
                console.log(data)
            }
          });
    });
//    drag and drop tops  //////////////// ///////////////// //////////// /////////

    // Can probably find a DRY method for adding draggable and droppable to the different areas.
    // The code is fairly similar minus accessing the classes for each
    $(".draggable_top").draggable({
        appendTo: ".ui_sortable",
        helper: "clone",
        drag: function () {
           console.log("dragging");
        }
    });

    $( ".droppable_top" ).droppable({
//        activeClass: 'ui-state-default',
        hoverClass: 'ui-state-hover',
        accept: ':not(.ui-sortable-helper)',
        drop: function( event, ui ) {
            $( this).find('.placeholder').remove();
            $("<li></li>").image(ui.draggable.image()).appendTo( this );
            console.log("dropped!");
        }
    });
//    drag and drop bottoms   /////////////////////      //////////////////
    $(".draggable_bottom").draggable({
        appendTo: ".ui_sortableA",
        helper: "clone",
        drag: function () {
           console.log("dragging");
        }
    });
    $( ".droppable_bottom" ).droppable({
        hoverClass: 'ui-state-hover',
        accept: ':not(.ui-sortable-helper)',
        drop: function( event, ui) {
            $( this).find('.spothold').remove();
            $("<li></li>").image(ui.draggable.image()).appendTo( this );
            console.log("dropped!");
        }
    });
//    drag and drop headwear    ////////////////////////     //////////
    $(".draggable_headwear").draggable({
        appendTo: ".ui_sortableHead",
        helper: "clone",
        drag: function () {
           console.log("dragging");
        }
    });
    $( ".droppable_headwear" ).droppable({
        hoverClass: 'ui-state-hover',
        accept: ':not(.ui-sortable-helper)',
        drop: function( event, ui ) {
            $( this).find('.spotheld').remove();
            $("<li></li>").image(ui.draggable.image()).appendTo( this );
            console.log("dropped!");
        }
    });
//    drag and drop shoes //////////////////////////////////////
    $(".draggable_shoes").draggable({
        appendTo: ".ui_sortableShoes",
        helper: 'clone',
        drag: function () {
           console.log("dragging");
        }
    });
    $( ".droppable_shoes" ).droppable({
        hoverClass: 'ui-state-hover',
        accept: ':not(.ui-sortable-helper)',
        drop: function( event, ui ) {
            $(this).find('.placehold').remove();
            $('<li></li>').image(ui.draggable.image()).appendTo(this);
            console.log("dropped!");
        }
    });
//    drag and drop accessories //////////////////////////////////////
    $(".draggable_accessories").draggable({
        appendTo: ".ui_sortableAcc",
        helper: 'clone',
        drag: function () {
           console.log("dragging");
        }
    });
    $( ".droppable_accessories" ).droppable({
        hoverClass: 'ui-state-hover',
        accept: ':not(.ui-sortable-helper)',
        drop: function( event, ui ) {
            $(this).find('.holdspot').remove();
            $('<li></li>').image(ui.draggable.image()).appendTo(this);
            console.log("dropped!");
        }
    });
});
