//just some random values i added 
var subjectObject = {
    "United Kingdom": {
        "Engineering": ["Electrical Engineering", "Chemical Engineering", "Biomedical Engineering", "Mechanical Engineering"],
        "Sciences": ["Biochemistry", "Physics", "Pharmacology", "Chemistry"],
        "Business": ["Accounting", "Finance", "Marketing", "Management"]
    },
    "Canada": {
        "History": ["Social History", "Political History", "Economic History"],
        "Arts": ["Film", "Music", "Theatre"]
    }
}
window.onload = function () {
    var countrySel = document.getElementById("country");
    var departmentSel = document.getElementById("department");
    var subjectSel = document.getElementById("subject");
    for (var x in subjectObject) {
        countrySel.options[countrySel.options.length] = new Option(x, x);
    }
    countrySel.onchange = function () {
        //empty Subjects- and Dropdowns- dropdowns
        subjectSel.length = 1;
        departmentSel.length = 1;
        //display correct values
        for (var y in subjectObject[this.value]) {
            departmentSel.options[departmentSel.options.length] = new Option(y, y);
        }
    }
    departmentSel.onchange = function () {
        //empty Subjects dropdown
        subjectSel.length = 1;
        //display correct values
        var z = subjectObject[countrySel.value][this.value];
        for (var i = 0; i < z.length; i++) {
            subjectSel.options[subjectSel.options.length] = new Option(z[i], z[i]);
        }
    }
}
