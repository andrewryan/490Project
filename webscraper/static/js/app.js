$(document).foundation()

document.getElementById("update").addEventListener("click", function(){
    console.log("UPDATE button worked");
    document.getElementById("update").style.display = "none";
    document.getElementById("spinner").style.visibility = "visible";

    $.ajax({
      url: '/runUpdate/',
    });

});
