function activateZoom() {

    let zoomImage = $('.image-container-inner').ZoomArea({
        zoomLevel: 1,
        minZoomLevel: 1,
        maxZoomLevel: 15,
        parentOverflow: 'auto',
        usedAnimateMethod: 'jquery'
    });
}


$(window).on("load", function () {
    activateZoom();
});
