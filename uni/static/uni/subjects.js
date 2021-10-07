document.addEventListener("DOMContentLoaded", function () {
  const divChange = document.querySelector("#addButton");
  let tutorChangeButtons = document.querySelectorAll(".tutorButton");
  let editSubjectButtons = document.querySelectorAll("#editButton");

  divChange.addEventListener("click", () => {
    if (document.getElementById("newSubj").style.display != "block") {
      document.getElementById("newSubj").style.display = "block";
      document.getElementById("subjects").style.display = "none";
      document.getElementById("editSubj").style.display = "none";
      divChange.className = "btn btn-danger";
      divChange.textContent = "Cancel";
    } else {
      location.reload();
    }
  });

  tutorChangeButtons.forEach((link) => {
    link.onclick = (e) => {
      let subjName = e.target.dataset.subjname;
      document.getElementById("subjName").innerHTML = subjName;
      document.getElementById("subjects").style.display = "none";
      document.getElementById("addButton").style.display = "none";
      document.getElementById("editSubj").style.display = "none";
      document.getElementById("assignTutor").style.display = "block";
    };
  });

  editSubjectButtons.forEach((link) => {
    link.onclick = (e) => {
      const id = e.target.dataset.subjid;
      const text = e.target.dataset.name;
      const desc = e.target.dataset.desc;
      document.getElementById("subjects").style.display = "none";
      document.getElementById("addButton").style.display = "none";
      document.getElementById("assignTutor").style.display = "none";
      document.getElementById("editSubj").style.display = "block";

      document.querySelector("#editName").value = text;
      document.querySelector("#editDesc").value = desc;

      const editS = document.querySelector("#editSubjForm");
      editS.onsubmit = function (event) {
        event.preventDefault();
        const newText = document.querySelector("#editName").value;
        const newDesc = document.querySelector("#editDesc").value;

        const csrftoken = getCookie("csrftoken");

        console.log(`{
          name : ${newText},
          id : ${id},
          description: ${newDesc},
        }`);

        fetch("/editSubject", {
          method: "POST",
          headers: {
            "X-CSRFToken": csrftoken,
          },
          body: JSON.stringify({
            id: id,
            name: newText,
            description: newDesc,
          }),
        })
          .then((response) => response.json())
          .then((result) => {
            // Print result
            console.log(result.message);
            alert(result.message);
          })
          .catch((error) => alert(error.error));

        document.querySelector(`#subjectName${id}`).innerHTML = newText;
        document.querySelector(`#subjectDesc${id}`).innerHTML = newDesc;

        document.getElementById("newSubj").style.display = "none";
        document.getElementById("addButton").style.display = "block";
        document.getElementById("subjects").style.display = "block";
        document.getElementById("editSubj").style.display = "none";
        location.reload();
      };
    };
  });

  const createSubj = document.querySelector("#subjForm");
  createSubj.onsubmit = addSubject;

  const addT = document.querySelector("#assignT");
  addT.onchange = addTutor;
});

function addSubject() {
  const text = document.querySelector("#sName").value;
  const desc = document.querySelector("#desc").value;

  const csrftoken = getCookie("csrftoken");

  console.log(`{
    name : ${text},
    description: ${desc},
  }`);

  fetch("/addSubject", {
    method: "POST",
    headers: {
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({
      name: text,
      description: desc,
    }),
  })
    .then((response) => response.json())
    .then((result) => {
      // Print result
      console.log(result);
      alert(result.message);
    })
    .catch((error) => alert(error.error));
  location.reload();
  return false;
}

function addTutor() {
  const subjName = document.querySelector("#subjName").innerHTML;
  const select = document.querySelector("#assignT");
  //https://ricardometring.com/getting-the-value-of-a-select-in-javascript
  const tutor = select.options[select.selectedIndex].text;

  const csrftoken = getCookie("csrftoken");

  console.log(`{
    Sname : ${subjName},
    Tname: ${tutor},
  }`);

  fetch("/assignTutor", {
    method: "POST",
    headers: {
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({
      sName: subjName,
      tName: tutor,
    }),
  })
    .then((response) => response.json())
    .then((result) => {
      // Print result
      console.log(result);
      alert(result.message);
    })
    .catch((error) => {
      console.log(error);
      alert(error.error);
    });
  window.location.href = "http://127.0.0.1:8000/subjects";
}

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
}
