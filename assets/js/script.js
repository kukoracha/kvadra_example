$(document).ready(function(){

    $("#txt").on("input", function(){
        $(this).removeClass("invalid");
    });


    /*Загрузка txt посрдеством API uploadtext*/
    $("#uploadtext").on("submit", function(e){
        e.preventDefault();
        var form = $(this);
        var txt = $("#txt", form).val().trim();
        if (txt.length === 0) {
            $("#txt", form).addClass("invalid");
            return;
        }
        $("button", form).attr("disabled", true);
        $.ajax({
            type: "POST",
            url: "/uploadtext/",
            data: {
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']", form).val(),
                txt: txt,
            },
            complete: function(){
                $("button", form).attr("disabled", false);
            },
        });
    });

    /*Получение txt посрдеством API gettext*/
    $(".collection-item").on("click", function(e){
        e.preventDefault();
        $(".collection-item").removeClass("active");
        $(this).addClass("active");
        var id = $(this).data("id");
        $.ajax({
            type: "GET",
            url: "/gettext/",
            data: {id: id},
            success: function(data){
                $(".view").html(data.txt);
            },
            error: function(){
                $(".view").html("Произошла ошибка при загрузке сообщения");
            },
        });
    });

});