function func(e){
  event.preventDefault();
}

function loadFile(){
    var fileInput = document.getElementById('fileInput');
    var file = fileInput.files[0];
    var reader = new FileReader();
  
    reader.onload = function(e) {
      var content = e.target.result;
      const textarea =  document.getElementById('textArea');
      textarea.value = content;
      if (!textarea.value.endsWith(content)) {
        textarea.value = content;
      }
    };
    reader.readAsText(file);
}
document.getElementById("mys").addEventListener("click", loadFile);

