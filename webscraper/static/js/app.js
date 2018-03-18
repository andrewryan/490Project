$(document).foundation()

document.getElementById("update").addEventListener("click", function(){
    console.log("UPDATE button worked");
    document.getElementById("update").style.display = "none";
    document.getElementById("spinner").style.visibility = "visible";

    $.ajax({
      url: '/runUpdate/',
    });
    setTimeout(function(){ window.location.reload() },10000)

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


// document.getElementById("update").addEventListener("click", function(){
//     console.log("UPDATE button worked");
//     // document.getElementById("update").style.display = "none";
//     // document.getElementById("spinner").style.visibility = "visible";
//
//     $.ajax({
//         url: '/runUpdate/',
//         data: {
//           'data': data
//         },
//         dataType: 'json',
//        success: function (data) {
//                remove spinner
//              reload page, iterate through returned "data" and pass it to html
//           // if (data.is_taken) {
//             // alert("A user with this username already exists.");
//           }
//         }
//       });
//
//     setTimeout(function(){ window.location.reload() },10000)
//
// });

// $(document).ajaxStart(function(){
//        timer = setTimeout(function(){
//           $(".elmt").addClass("loading");
//        },1500);
//     });
//
//     $(document).ajaxStop(function(){
//       clearTimeout(timer);
//       $(".elmt").removeClass("loading");
//     });

// $(document).ajaxStop(function () {
//         $('#loading').hide();
//     });
//
//     $(document).ajaxStart(function () {
//         $('#loading').show();
//     });
