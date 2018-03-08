$(document).foundation()

document.getElementById("update").addEventListener("click", function(){
    // console.log("Hello World!");
    $.ajax({
      url: '/runscript/',
      // data: {
      //   'properties': properties
      // },
      // dataType: 'json',
      // success: function (data) {
      //   if (data.is_taken) {
      //     alert("A user with this username already exists.");
      //   }
      // }
    });
});
