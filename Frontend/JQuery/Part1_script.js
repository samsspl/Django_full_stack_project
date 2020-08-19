//use $ to grab tags/items using jQuery 

var h = $('h1');  //h1 tag
h.css('color', 'green'); //h1 color to green
h.css('background', '#fed8b1'); //bg color in hex for h1

// passing in multiple css arguments

var newObj_Css = {
    'color':'white',
    'background':"grey",
    'border':'3px solid rgb(170 1 20)'
}
var cssObjList = {
    'color':'#006400', //dark green
}

var para = $('p'); // ptag

para.css(newObj_Css); // multiple css in one go.

var listItem = $('li');// not the same js array.

listItem.css(cssObjList); //css applied to all list item.

listItem.eq(0).css('color', 'orange'); // selecting item inside list (first item)
listItem.eq(-1).css('color', 'orange'); // selecting item inside list (last item)

//editing text inside tags 
//to use strong, em tag, one must call html instead of text
var hText = h.html(h.text() + '<strong><em> Edited later in js!</em></strong>'); 

var inPuttag = $('input'); //both input tag was grab
// initial val "Enter Your Name" in html
inPuttag.eq(0).attr('placeholder','Enter Your Full Name!');

listItem.eq(2).addClass('turnRed'); //class turnRed is define in html
// listItem.eq(2).removeClass('turnRed'); //uncomment to see the changes

//toggle instead of add/remove class, use toggle second time for removing effects

listItem.eq(3).toggleClass('turnBlue'); 
// listItem.eq(3).toggleClass('turnBlue');

