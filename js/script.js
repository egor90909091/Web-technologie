
function toggleContent(element) {
  var content = element.nextElementSibling.querySelector('p');
  if (content.style.display === "block") {
    content.style.display = "none";
  } else {
    content.style.display = "block";
  }
}
