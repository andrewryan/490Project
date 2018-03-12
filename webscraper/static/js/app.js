$(document).foundation()

document.getElementById("update").addEventListener("click", function(){
    console.log("UPDATE button worked");
    document.getElementById("update").style.display = "none";
    document.getElementById("spinner").style.visibility = "visible";

    $.ajax({
      url: '/runUpdate/',
    });
    setTimeout(function(){ window.location.reload() },6000)

});

document.getElementById("search").addEventListener("click", function(){
   var category = document.getElementById("category").value;
   var ownerAge = document.getElementById("ownerAge").value;
   var equityValue = document.getElementById("equityValue").value;
   var occupied = document.getElementById("occupied").value;
   var lastSale = document.getElementById("lastSale").value;
   console.log("SEARCH button worked");
   console.log(category);
   console.log(ownerAge);
   console.log(equityValue);
   console.log(occupied);
   console.log(lastSale);

    // $.ajax({
    //   url: '/runUpdate/',
    // });
    // setTimeout(function(){ window.location.reload() },6000)

});
