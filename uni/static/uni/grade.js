document.addEventListener("DOMContentLoaded", function () {
  let getGradeButton = document.querySelectorAll("#getGrade");
  getGradeButton.forEach((link) => {
      link.onclick = (e) => {
        const id = e.target.dataset.subj_id
        const gradeText = document.getElementById(`subjectGrade/${id}`)
        fetch(`/getGrade/${id}`)
        .then((response) => response.json())
        .then((data) => {
            console.log(data)
            gradeText.innerHTML = data
        }).catch((error) => {
          console.log(error)
          alert(error.error)
        });
      }
  });
  
  let editGradeButtons = document.querySelectorAll("#editGradeButton");

  editGradeButtons.forEach((link) => {
    link.onclick = (e) => {
      let subjID = e.target.dataset.subj_id;
      let studentID = e.target.dataset.student_id;
      let studentName = e.target.dataset.student_name;

      document.getElementById("subjStudents").style.display = "none";
      document.getElementById("editGrade").style.display = "block";
      document.getElementById("studentName").innerHTML = studentName;

      document.getElementById("editGradeForm").onsubmit = () => {
        const grade = document.querySelector("#editGradeText").value;

        const csrftoken = getCookie("csrftoken");

        console.log(`{
            grade : ${grade},
            subjID : ${subjID},
            studentID : ${studentID},
        }`);

        fetch("/submitGrade", {
          method: "POST",
          headers: {
            "X-CSRFToken": csrftoken,
          },
          body: JSON.stringify({
            grade: grade,
            subjID: subjID,
            studentID: studentID,
          }),
        })
          .then((response) => response.json())
          .then((result) => {
            // Print result
            console.log(result);
            alert(result.message)
          })
          .catch((error) => console.log(error));
        location.reload();
        return false;
      };
    };
  });
});

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
}
