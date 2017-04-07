/**
 * Created by QXT on 2017/4/5.
 */
(function(){
    $('.up').on('click',function(){
        var ww = $(window).width();
        //pc
        if(ww>1200){
            if($(".up").hasClass('n1')){
                $('.up').css({"margin-bottom":"30px"});
                $(".up").removeClass('n1');
                $(".up").html('↑');
                $('.title').css({"height":"0px"});
                $('.context').css({"top":"30%"})
            }else{
                $('.up').css({"margin-bottom":"320px"});
                $(".up").addClass('n1');
                $('.title').css({"height":"380px"});
                $('.context').css({"top":"14%"})
                $(".up").html('↓');
            }
        }
        //pad
        else if(769<ww<1200){
            if($(".up").hasClass('n1')){
                $('.up').css({"margin-bottom":"30px"});
                $(".up").removeClass('n1');
                $(".up").html('↑');
                $('.title').css({"height":"0px"});
                $('.context').css({"top":"30%"})
            }else{
                $('.up').css({"margin-bottom":"360px"});
                $(".up").addClass('n1');
                $('.title').css({"height":"420px"});
                $('.context').css({"top":"25%"});
                $(".up").html('↓');
            }
        }
        else if(ww<769){
            if($(".up").hasClass('n1')){
                $('.up').css({"margin-bottom":"30px"});
                $(".up").removeClass('n1');
                $(".up").html('↑');
                $('.title').css({"height":"0px"});
                $('.context').css({"top":"30%"})
            }else{
                $('.up').css({"margin-bottom":"390px"});
                $(".up").addClass('n1');
                $('.title').css({"height":"450px"});
                $('.context').css({"top":"18%"});
                $(".up").html('↓')
            }
        }
        else{

        }
    })
}());
