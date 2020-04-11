$(function() {

  $(".nav-resp-menus-cont").slideUp();

  $(".resp-btn").click(function(){
    $(".nav-resp-menus-cont").slideToggle();
  });

  $("#courses-menu").click(function(){
    $("#courses-menus").slideToggle();
  });

  $("#admission-menu").click(function(){
    $("#admission-menus").slideToggle();
  });

  var imageFolder = "/img/gallery/megaleio/"
  var j = 1;
  for (var i = 1; i <= 15; i=i+3) {

  	var img1 = imageFolder+i+".jpg";
  	var img2 = imageFolder+(i+1)+".jpg";
  	var img3 = imageFolder+(i+2)+".jpg";
    
  	$('.megaleio-gal-cont').append("<div class='row gal-row-cont gal-row-cont"+j+"'>");
  	$('.gal-row-cont'+j).append("<div class='img-responsive gal-img' style='background-image: url("+img1+");'></div>");
  	$('.gal-row-cont'+j).append("<div class='img-responsive gal-img' style='background-image: url("+img2+");'></div>");
  	$('.gal-row-cont'+j).append("<div class='img-responsive gal-img' style='background-image: url("+img3+");'></div>");
  	$('.megaleio-gal-cont').append('</div>');
  	
    j=j+1;
  }

  

});

