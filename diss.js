var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var myObj = JSON.parse(this.responseText);
    }
};
xmlhttp.open("GET", "main.php", true);
xmlhttp.send();



var htmlpage = new XMLHttpRequest();
htmlpage.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var myObj2 = this.responseText;
    }
};
htmlpage.open("GET", "pagehtml.php", true);
htmlpage.send();





