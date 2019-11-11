function openForm() {
  document.getElementById("myForm").style.display = "block";
  }
  
function closeForm() {
  document.getElementById("myForm").style.display = "none";
  }
  window.onclick = function(event) {
    if (event.target == document.getElementById("myForm")) {
      document.getElementById("myForm").style.display = "none";
    }
  }