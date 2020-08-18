// $('h1').click(function () {
//     console.log('There was a click!'); 
//     $(this).html($(this).text() + '<strong><em> Edited this in js using jQuery!</em></strong>');
// })

$('li').click(function () {
    console.log('any li was clicked!');
})

// keyboard 

$('input').eq(0).keypress(function (event) {
    
    console.log(event); // check console.
    if(event.which === 13){  //when you press enter, h3 will toggle blue
        $('h3').toggleClass('turnBlue');
    }
})

//on()

$('h1').on('dblclick', function () {
    $(this).toggleClass('turnRed'); 
})

$('h2').on('mouseenter', function () {
    $(this).toggleClass('turnRed'); 
})

$('input').eq(1).on('click',function () {  // clicking submit will fadeout all items inside .container 
    $('.container').fadeOut(3000);
})