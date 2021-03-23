$(document).ready(function () {
    $("#input-file").change(function () {
        $('.c-glitch').attr('style', 'background-image:url("' + URL.createObjectURL(event.target.files[0]) + '")');
        $('.c-glitch__img').attr('style', 'background-image:url("' + URL.createObjectURL(event.target.files[0]) + '")');
    });

    $("#analyze").on('click', function () {
        //Resim var mı diye kontrol ediyoruz. 
        if ($('.c-glitch').attr("style")) {

            //Sıkıntı olmasın diye butonlar kapandı
            //$('.btn,.btn-lg,.btn-default').hide();




            //length attribute' ü o nesnenin sayısını değil var olup olmadığını dönderir: varsa return 1 yoksa return 0 
            if ($('.style_file').length == 0) {
                //Resme işleniyor animasyonu ekleniyor.
                $('<link />', {
                    id: 'style_file',
                    rel: 'stylesheet',
                    href: "./static/css/animation.css"
                }).appendTo('head');
            }
            var form_data = new FormData($('#upload-file')[0]);

            $('#input-file').prop( "disabled", true );
            $('#analyze').prop( "disabled", true );


            $.ajax({
                type: 'POST',
                url: '/predict',
                data: form_data,
                contentType: false,
                cache: false,
                processData: false,
                async: true,
                success: function (data) {
                    console.log("Fonksiyon başarıyla çalıştı:" + data);

                    $('#result').html(data.replaceAll("\n", "<br>"));


                    //$('.btn,.btn-lg,.btn-default').show();
                    $('#input-file').prop( "disabled", false );
                    $('#analyze').prop( "disabled", false );
                    $("#style_file").remove();
                },
            });

        } else {
            alert("Önce Resim Seçiniz");
        }
    });
});
