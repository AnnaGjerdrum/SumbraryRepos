function filterSearch() {
  var input, filter, table, tr, td, i;
  input = document.getElementById("searchInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("searchTable");
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[0];
      if (td) {
        if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
}

function subject(id) {
  document.location = "../subject/"+id+"/"
}

function book(id) {
  document.location = "../book/"+id+"/"
}

function uni(id) {
  document.location = "../university/"+id+"/"
}

function summary(id) {
  document.location = "../summary/"+id+"/"
}
