//jQuery code
jQuery(function($) {
	"use strict";

  $(".nav-toggle-btn").on('click', function(e) {
    e.preventDefault();
    $(".nav").slideToggle();
  });
    /* end drop nav */

  $('.amount__btn_minus').click(function () {
    var $input = $(this).parent().find('input');
    var count = parseInt($input.val()) - 1;
    count = count < 1 ? 1 : count;
    $input.val(count);
    $input.change();
    return false;
  });
  
  $('.amount__btn_plus').click(function () {
    var $input = $(this).parent().find('input');
    $input.val(parseInt($input.val()) + 1);
    $input.change();
    return false;
  });

    if($(".main-slider").length){
        $(".main-slider").bxSlider({
            mode: 'vertical',
            controls: false
        });
    }

    if($(".people-slider").length){
        $(".people-slider").bxSlider({
            pager: false,
            slideWidth: 192,
            minSlides: 1,
            maxSlides: 5,
            moveSlides: 1,
            nextSelector: '.slider-controls__next',
            prevSelector: '.slider-controls__prev',
        });
    }
  	/* End slider */

    if($(".slider").length){
        $(".slider").bxSlider({
            slideWidth: 240,
            minSlides: 1,
            maxSlides: 4,
            moveSlides: 1,
            pager: false,
            nextSelector: '.slider-controls__next',
            prevSelector: '.slider-controls__prev',
        });
    }
    /* End best offers */

    if($('.testimonials-slider').length){
        $('.testimonials-slider').bxSlider({
            pager: false,
            slideWidth: 190,
            minSlides: 1,
            maxSlides: 3,
            moveSlides: 1
        });
    }
    /* end testimonial slider */

    if($(".tabs").length){
        $(".tabs").tabs();
    }
  	/* End jQuery UI tabs */

    if($('.tweets-slider').length){
        $('.tweets-slider').bxSlider({
            mode: 'vertical',
            pager: false
        });
    }
    /* end tweets slider */


    if($('.video-popup').length){
        $('.video-popup').magnificPopup({
            disableOn: 700,
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: false,

            fixedContentPos: false
        });
    }
  /* end video popup */


    if($('.statistics__circle').length){
        $('.statistics__circle').circliful();
    }
  /* circle statistic */
});
