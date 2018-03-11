$(document).foundation()

document.getElementById("update").addEventListener("click", function(){
    console.log("update button worked");
    document.getElementById("update").style.display = "none";
    document.getElementById("spinner").style.visibility = "visible";

    $.ajax({
      url: '/runUpdate/',
    });
    setTimeout(function(){ window.location.reload() },4000)

});
