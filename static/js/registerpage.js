function openForm() {
  var popup = document.getElementById("myForm");
  popup.classList.toggle("show");
}
  
function closeForm() {
  document.getElementById("myForm").style.display = "none";
  }
  window.onclick = function(event) {
    if (event.target == document.getElementById("myForm")) {
      document.getElementById("myForm").style.display = "none";
    }
  }