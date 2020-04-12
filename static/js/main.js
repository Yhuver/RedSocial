
(function ($) {
    "use strict";

    /*==================================================================
    [ Validate after type ]*/
    $('.validate-input .input100').each(function(){
        $(this).on('blur', function(){
            if(validate(this) == false){
                showValidate(this);
            }
            else {
                $(this).parent().addClass('true-validate');
            }
        })    
    })
  
  
    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit',function(){
        var check = true;

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
        }

        return check;
    });


    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
           $(this).parent().removeClass('true-validate');
        });
    });

     function validate (input) {
        if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(input).val().trim() == ''){
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');

        $(thisAlert).append('<span class="btn-hide-validate">&#xf135;</span>')
        $('.btn-hide-validate').each(function(){
            $(this).on('click',function(){
               hideValidate(this);
            });
        });
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();
        $(thisAlert).removeClass('alert-validate');
        $(thisAlert).find('.btn-hide-validate').remove();
    }
    
    window.onscroll = function (e) {  
    var otherScrollTop = document.documentElement.scrollTop; //IE & Firefox
    var otherScrollLeft = document.documentElement.scrollLeft; //IE & Firefox
    //alert(otherScrollTop + " - " + otherScrollLeft);

    if (otherScrollTop < 50) {
        document.getElementById("myDIV").style.opacity = "0";
    } else if ( otherScrollTop < 100) {
        document.getElementById("myDIV").style.opacity = "0.2";
    } else if ( otherScrollTop < 150) {
        document.getElementById("myDIV").style.opacity = "0.4";
    }
    else if ( otherScrollTop < 200) {
        document.getElementById("myDIV").style.opacity = "0.6";
    }
    else if ( otherScrollTop < 250) {
        document.getElementById("myDIV").style.opacity = "0.8";
    }     
    else if ( otherScrollTop > 251) {

  document.getElementById("myDIV").style.opacity = "1";
    }
    }
  

})(jQuery);