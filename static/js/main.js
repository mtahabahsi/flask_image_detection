var loadFile = function (event) {
    console.log(URL.createObjectURL(event.target.files[0]));
    $('.c-glitch').attr('style', 'background-image:url("' + URL.createObjectURL(event.target.files[0]) + '")');
    $('.c-glitch__img').attr('style', 'background-image:url("' + URL.createObjectURL(event.target.files[0]) + '")');
};



$(document).ready(function () {
    $("#analyze").on('click', function () {
        $('<link />', {
            id: 'style_file',
            rel: 'stylesheet',
            href: "./static/css/animation.css"
        }).appendTo('head');

    });
});